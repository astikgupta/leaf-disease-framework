"""
evaluate.py  —  Evaluate trained MobileNetV2 on the PlantVillage validation set
Usage:
    python evaluate.py
    python evaluate.py --data_dir data/plantvillage/color --model_dir models
"""

import os
import json
import argparse
import copy

import torch
import torch.nn as nn
import torchvision.transforms as transforms
import torchvision.models as models
from torchvision import datasets
from sklearn.metrics import (classification_report, confusion_matrix,
                             accuracy_score, f1_score)
import numpy as np
import matplotlib
matplotlib.use("Agg")          # non-interactive backend
import matplotlib.pyplot as plt
from tqdm import tqdm


def parse_args():
    parser = argparse.ArgumentParser(description="Evaluate PlantVillage model")
    parser.add_argument("--data_dir",   default="data/plantvillage/color")
    parser.add_argument("--model_dir",  default="models")
    parser.add_argument("--batch_size", type=int, default=32)
    parser.add_argument("--val_split",  type=float, default=0.2)
    parser.add_argument("--num_workers",type=int, default=2)
    return parser.parse_args()


def load_model_and_classes(model_dir, device):
    class_names_path = os.path.join(model_dir, "class_names.json")
    weights_path     = os.path.join(model_dir, "plant_disease_model.pth")

    if not os.path.exists(class_names_path):
        raise FileNotFoundError(f"class_names.json not found in {model_dir}. "
                                "Run train.py first.")
    if not os.path.exists(weights_path):
        raise FileNotFoundError(f"plant_disease_model.pth not found in {model_dir}. "
                                "Run train.py first.")

    with open(class_names_path) as f:
        class_names = json.load(f)

    num_classes = len(class_names)
    model = models.mobilenet_v2(weights=None)
    model.classifier[1] = nn.Linear(model.last_channel, num_classes)
    model.load_state_dict(torch.load(weights_path, map_location=device))
    model = model.to(device)
    model.eval()
    return model, class_names


def build_val_loader(data_dir, val_split, batch_size, num_workers):
    val_transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406],
                             std=[0.229, 0.224, 0.225]),
    ])

    full_dataset = datasets.ImageFolder(root=data_dir, transform=val_transform)
    total_size   = len(full_dataset)
    val_size     = int(total_size * val_split)
    train_size   = total_size - val_size

    _, val_dataset = torch.utils.data.random_split(
        full_dataset, [train_size, val_size],
        generator=torch.Generator().manual_seed(42))

    val_loader = torch.utils.data.DataLoader(
        val_dataset, batch_size=batch_size,
        shuffle=False, num_workers=num_workers)
    return val_loader, val_size


def save_confusion_matrix(cm, class_names, output_path):
    fig, ax = plt.subplots(figsize=(20, 18))
    im = ax.imshow(cm, interpolation="nearest", cmap=plt.cm.Blues)
    plt.colorbar(im, ax=ax)

    tick_marks = np.arange(len(class_names))
    short_names = [c.replace("___", "\n") for c in class_names]
    ax.set_xticks(tick_marks)
    ax.set_xticklabels(short_names, rotation=90, fontsize=6)
    ax.set_yticks(tick_marks)
    ax.set_yticklabels(short_names, fontsize=6)

    ax.set_ylabel("True label",      fontsize=12)
    ax.set_xlabel("Predicted label", fontsize=12)
    ax.set_title("Confusion Matrix — PlantVillage", fontsize=14)
    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    plt.close()
    print(f"  Confusion matrix saved → {output_path}")


def main():
    args   = parse_args()
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Using device: {device}\n")

    # Load model
    model, class_names = load_model_and_classes(args.model_dir, device)
    print(f"Model loaded. Classes: {len(class_names)}\n")

    # Build val loader
    val_loader, val_size = build_val_loader(
        args.data_dir, args.val_split, args.batch_size, args.num_workers)
    print(f"Validation samples: {val_size}\n")

    # Inference
    all_preds  = []
    all_labels = []

    with torch.no_grad():
        for inputs, labels in tqdm(val_loader, desc="Evaluating", unit="batch"):
            inputs = inputs.to(device)
            outputs = model(inputs)
            _, preds = torch.max(outputs, 1)
            all_preds.extend(preds.cpu().numpy())
            all_labels.extend(labels.numpy())

    # Metrics
    acc = accuracy_score(all_labels, all_preds)
    f1  = f1_score(all_labels, all_preds, average="weighted")

    print("\n" + "="*60)
    print("  EVALUATION RESULTS")
    print("="*60)
    print(f"  Overall Accuracy  : {acc*100:.2f}%")
    print(f"  Weighted F1-Score : {f1*100:.2f}%")
    print("\n  Per-class report:")
    print(classification_report(all_labels, all_preds,
                                target_names=class_names, digits=3))

    # Confusion matrix
    cm = confusion_matrix(all_labels, all_preds)
    os.makedirs(args.model_dir, exist_ok=True)
    cm_path = os.path.join(args.model_dir, "confusion_matrix.png")
    save_confusion_matrix(cm, class_names, cm_path)

    print("="*60)
    print(f"\n✅ Evaluation complete!")


if __name__ == "__main__":
    main()
