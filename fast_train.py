"""
fast_train.py  —  Trains on a small RANDOM SUBSET of PlantVillage for quick results.
Recommended for CPU users who want to see the app working in <1 hour.
"""

import os
import argparse
import torch
import torch.nn as nn
from torchvision import datasets, models
import train # Import logic from our main training script
import random
from torch.utils.data import Subset

def main():
    parser = argparse.ArgumentParser(description="Fast Subset Training")
    parser.add_argument("--subset_pct", type=float, default=0.05, help="Percentage of data to use (0.01 to 1.0)")
    parser.add_argument("--epochs", type=int, default=3)
    parser.add_argument("--data_dir", default="data/plantvillage/color")
    args = parser.parse_args()

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Running FAST TRAINING on {device} using {args.subset_pct*100}% of data.")

    # 1. Load Data
    train_tf, val_tf = train.get_transforms()
    full_dataset = datasets.ImageFolder(root=args.data_dir, transform=train_tf)
    
    # 2. Create Subset
    num_total = len(full_dataset)
    num_subset = int(num_total * args.subset_pct)
    indices = random.sample(range(num_total), num_subset)
    subset_dataset = Subset(full_dataset, indices)
    
    # 3. Split Subset into Train/Val
    val_size = int(len(subset_dataset) * 0.2)
    train_size = len(subset_dataset) - val_size
    train_ds, val_ds = torch.utils.data.random_split(subset_dataset, [train_size, val_size])

    # 4. Dataloaders
    dataloaders = {
        "train": torch.utils.data.DataLoader(train_ds, batch_size=32, shuffle=True, num_workers=2),
        "val":   torch.utils.data.DataLoader(val_ds,   batch_size=32, shuffle=False, num_workers=2)
    }
    dataset_sizes = {"train": train_size, "val": val_size}

    # 5. Model
    model = train.build_model(len(full_dataset.classes), device)
    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
    scheduler = torch.optim.lr_scheduler.StepLR(optimizer, step_size=2, gamma=0.1)

    # 6. Train
    model, history = train.train_model(
        model, dataloaders, dataset_sizes, criterion, optimizer, scheduler,
        device, args.epochs, "models"
    )

    # 7. Save
    import json
    torch.save(model.state_dict(), "models/plant_disease_model.pth")
    with open("models/class_names.json", "w") as f:
        json.dump(full_dataset.classes, f)
    
    print("\n✅ Fast training complete! Try the app now.")

if __name__ == "__main__":
    main()
