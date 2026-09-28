#!/usr/bin/env python3
"""Sync dotfiles and app configs."""
import argparse, os, shutil, json

CONFIG_DIR = os.path.join(os.path.dirname(__file__), "data")

def pull():
    for f in os.listdir(CONFIG_DIR):
        src = os.path.join(CONFIG_DIR, f)
        dst = os.path.expanduser(f"~/.config/{f}")
        shutil.copy2(src, dst)
        print(f"  {f} -> {dst}")

def push():
    for f in os.listdir(os.path.expanduser("~/.config")):
        src = os.path.expanduser(f"~/.config/{f}")
        if os.path.isfile(src):
            dst = os.path.join(CONFIG_DIR, f)
            shutil.copy2(src, dst)
            print(f"  {f} -> data/{f}")

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--pull", action="store_true")
    p.add_argument("--push", action="store_true")
    args = p.parse_args()
    if args.pull: pull()
    elif args.push: push()
    else: p.print_help()
