"""
train.py  —  Train MobileNetV2 on the PlantVillage dataset
Usage:
    python train.py
    python train.py --data_dir data/plantvillage/color --epochs 15 --batch_size 64
"""

import os
import json
import argparse
import time
import copy

import torch
import torch.nn as nn
import torch.optim as optim
from torch.optim import lr_scheduler
import torchvision
import torchvision.transforms as transforms
from torchvision import datasets, models
from tqdm import tqdm


# -------------------------------------------------------------------
# 1.  Parse command-line arguments
# -------------------------------------------------------------------
def parse_args():
    parser = argparse.ArgumentParser(description="Train MobileNetV2 on PlantVillage")
    parser.add_argument("--data_dir",   default="data/plantvillage/color",
                        help="Path to PlantVillage colour folder (contains class sub-folders)")
    parser.add_argument("--epochs",     type=int, default=10,
                        help="Number of training epochs (default: 10)")
    parser.add_argument("--batch_size", type=int, default=32,
                        help="Batch size (default: 32)")
    parser.add_argument("--lr",         type=float, default=0.001,
                        help="Learning rate (default: 0.001)")
    parser.add_argument("--val_split",  type=float, default=0.2,
                        help="Fraction of data used for validation (default: 0.2)")
    parser.add_argument("--output_dir", default="models",
                        help="Directory to save model weights and class names (default: models)")
    parser.add_argument("--num_workers",type=int, default=2,
                        help="DataLoader worker processes (default: 2)")
    return parser.parse_args()


# -------------------------------------------------------------------
# 2.  Data transforms
# -------------------------------------------------------------------
def get_transforms():
    train_transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.RandomHorizontalFlip(),
        transforms.RandomVerticalFlip(),
        transforms.RandomRotation(15),
        transforms.ColorJitter(brightness=0.2, contrast=0.2,
                               saturation=0.2, hue=0.1),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406],
                             std=[0.229, 0.224, 0.225]),
    ])
    val_transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406],
                             std=[0.229, 0.224, 0.225]),
    ])
    return train_transform, val_transform


# -------------------------------------------------------------------
# 3.  Build model
# -------------------------------------------------------------------
def build_model(num_classes: int, device: torch.device):
    model = models.mobilenet_v2(weights=models.MobileNet_V2_Weights.DEFAULT)
    # Replace the classifier head for our number of classes
    model.classifier[1] = nn.Linear(model.last_channel, num_classes)
    model = model.to(device)
    return model


# -------------------------------------------------------------------
# 4.  Training loop
# -------------------------------------------------------------------
def train_model(model, dataloaders, dataset_sizes, criterion, optimizer,
                scheduler, device, num_epochs, output_dir):
    best_model_wts = copy.deepcopy(model.state_dict())
    best_acc = 0.0

    history = {"train_loss": [], "train_acc": [],
               "val_loss":   [], "val_acc":   []}

    print("\n" + "="*60)
    print(f"  Training for {num_epochs} epochs on {device}")
    print("="*60)

    for epoch in range(num_epochs):
        t0 = time.time()
        print(f"\nEpoch {epoch+1}/{num_epochs}")
        print("-" * 40)

        for phase in ["train", "val"]:
            model.train() if phase == "train" else model.eval()

            running_loss   = 0.0
            running_correct = 0

            loop = tqdm(dataloaders[phase],
                        desc=f"  {phase.capitalize():5s}",
                        leave=True,
                        unit="batch")

            for inputs, labels in loop:
                inputs = inputs.to(device)
                labels = labels.to(device)

                optimizer.zero_grad()

                with torch.set_grad_enabled(phase == "train"):
                    outputs = model(inputs)
                    loss    = criterion(outputs, labels)
                    _, preds = torch.max(outputs, 1)

                    if phase == "train":
                        loss.backward()
                        optimizer.step()

                running_loss    += loss.item() * inputs.size(0)
                running_correct += torch.sum(preds == labels).item()

                loop.set_postfix(loss=loss.item())

            if phase == "train":
                scheduler.step()

            epoch_loss = running_loss    / dataset_sizes[phase]
            epoch_acc  = running_correct / dataset_sizes[phase]

            history[f"{phase}_loss"].append(epoch_loss)
            history[f"{phase}_acc"].append(epoch_acc)

            print(f"  {phase.capitalize():5s}  Loss: {epoch_loss:.4f}  "
                  f"Acc: {epoch_acc*100:.2f}%")

            if phase == "val" and epoch_acc > best_acc:
                best_acc = epoch_acc
                best_model_wts = copy.deepcopy(model.state_dict())
                # Save intermediate best
                os.makedirs(output_dir, exist_ok=True)
                torch.save(best_model_wts,
                           os.path.join(output_dir, "plant_disease_model.pth"))
                print(f"  ✅ New best model saved  (val acc = {best_acc*100:.2f}%)")

        elapsed = time.time() - t0
        print(f"  Epoch time: {elapsed:.1f}s")

    print("\n" + "="*60)
    print(f"  Training complete!  Best val acc: {best_acc*100:.2f}%")
    print("="*60)

    model.load_state_dict(best_model_wts)
    return model, history


# -------------------------------------------------------------------
# 5.  Main
# -------------------------------------------------------------------
def main():
    args = parse_args()

    # Safety checks
    if not os.path.isdir(args.data_dir):
        print(f"\n❌ ERROR: Data directory not found: '{args.data_dir}'")
        print("   Please download PlantVillage dataset and point --data_dir to the")
        print("   folder that contains the class sub-folders (e.g. Tomato___Early_blight)")
        print("   See README.md for download instructions.\n")
        return

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Using device: {device}")
    if device.type == "cuda":
        print(f"GPU: {torch.cuda.get_device_name(0)}")

    # ------------------------------------------------------------------
    # Load full dataset and split into train / val
    # ------------------------------------------------------------------
    train_tf, val_tf = get_transforms()

    full_dataset = datasets.ImageFolder(root=args.data_dir,
                                        transform=train_tf)
    class_names  = full_dataset.classes
    num_classes  = len(class_names)
    print(f"\nClasses found: {num_classes}")
    for i, c in enumerate(class_names):
        print(f"  [{i:02d}] {c}")

    # Split
    total_size = len(full_dataset)
    val_size   = int(total_size * args.val_split)
    train_size = total_size - val_size

    train_dataset, val_dataset = torch.utils.data.random_split(
        full_dataset, [train_size, val_size],
        generator=torch.Generator().manual_seed(42))

    # Apply val transform to val subset
    val_dataset.dataset = copy.deepcopy(full_dataset)
    val_dataset.dataset.transform = val_tf

    dataloaders = {
        "train": torch.utils.data.DataLoader(
            train_dataset, batch_size=args.batch_size,
            shuffle=True,  num_workers=args.num_workers, pin_memory=True),
        "val":   torch.utils.data.DataLoader(
            val_dataset,   batch_size=args.batch_size,
            shuffle=False, num_workers=args.num_workers, pin_memory=True),
    }
    dataset_sizes = {"train": train_size, "val": val_size}

    # ------------------------------------------------------------------
    # Build model, loss, optimiser, scheduler
    # ------------------------------------------------------------------
    model     = build_model(num_classes, device)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=args.lr)
    sched     = lr_scheduler.StepLR(optimizer, step_size=4, gamma=0.5)

    # ------------------------------------------------------------------
    # Train
    # ------------------------------------------------------------------
    model, history = train_model(
        model, dataloaders, dataset_sizes,
        criterion, optimizer, sched,
        device, args.epochs, args.output_dir)

    # ------------------------------------------------------------------
    # Save final weights + class mapping
    # ------------------------------------------------------------------
    os.makedirs(args.output_dir, exist_ok=True)
    weights_path     = os.path.join(args.output_dir, "plant_disease_model.pth")
    class_names_path = os.path.join(args.output_dir, "class_names.json")

    torch.save(model.state_dict(), weights_path)
    with open(class_names_path, "w") as f:
        json.dump(class_names, f, indent=2)

    print(f"\n✅ Model weights saved  → {weights_path}")
    print(f"✅ Class names saved    → {class_names_path}")
    print(f"\n  Final training history:")
    for ep in range(args.epochs):
        print(f"  Epoch {ep+1:02d}: "
              f"train_acc={history['train_acc'][ep]*100:.2f}%  "
              f"val_acc={history['val_acc'][ep]*100:.2f}%")


if __name__ == "__main__":
    main()
