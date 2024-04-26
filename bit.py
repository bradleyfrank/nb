#!/usr/bin/env python3

import argparse
import functools
import shlex
import subprocess
import sys
from contextlib import contextmanager
from pathlib import Path
from typing import Callable, ParamSpec, TypeVar


ENDC = "\033[0m"
RED = "\033[91m"
P = ParamSpec('P')
R = TypeVar('R')


def proc(cmd: str) -> str | bool:
  output = subprocess.run(shlex.split(cmd), capture_output=True)
  success = True if output.returncode == 0 else False
  return False if not success else output.stdout.decode("utf-8")


@contextmanager
def working_directory(directory -> PosixPath) -> None:
  cwd = Path.cwd()
  try:
    os.chdir(directory)
    yield directory
  finally:
    os.chdir(cwd)


def git_toplevel(func: Callable[P, R]) -> Callable[P, R]:
  @functools.wraps(func)
  def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
    if not (toplevel := proc("git rev-parse --show-toplevel")):
      print(f"{RED}Not in a git repo{ENDC}")
      sys.exit(1)
    kwargs["toplevel"] = toplevel
    return func(*args, **kwargs)
  return wrapper


@git_toplevel
def branch(*args, **kwargs):
  print(kwargs["toplevel"])



def clone():
  pass


@git_toplevel
def delete():
  pass


@git_toplevel
def pull():
  pass


@git_toplevel
def stash():
  pass


def parse_args() -> argparse.ArgumentParser:
  args = argparse.ArgumentParser(prog="bit")
  subparsers = args.add_subparsers(help="Subcommands", dest="subcommand")

  args.add_argument(
    "-t", "--tmux",
    help="Where tmux should open selection",
    choices=["session", "window", "pane", "current"], default="window"
  )

  cmd_branch = subparsers.add_parser("branch", help="Create new worktree branch")
  cmd_branch.set_defaults(func=branch)
  cmd_branch.add_argument("-n", "--name", help="Branch name", type=str, default=None)

  cmd_clone = subparsers.add_parser("clone", help="Clone a remote repo")
  cmd_clone.set_defaults(func=pull)
  cmd_clone_by_url = cmd_clone.add_argument_group("Clone any remote by URL")
  cmd_clone_by_url.add_argument("-u", "--url", help="Full repo URL", type=str, default=None)
  cmd_clone_by_name = cmd_clone.add_argument_group("Clone GitHub remote by org and name")
  cmd_clone_by_name .add_argument("-o", "--org", help="Org name", type=str, default=None)
  cmd_clone_by_name .add_argument("-n", "--name", help="Repo name", type=str, default=None)

  cmd_delete = subparsers.add_parser("delete", help="Delete a worktree", aliases=["rm"])
  cmd_delete.set_defaults(func=delete)
  cmd_delete.add_argument("-n", "--name", help="Worktree name", type=str, default=None)

  cmd_pull = subparsers.add_parser("pull", help="Pull a remote branch")
  cmd_pull.set_defaults(func=pull)
  cmd_pull.add_argument("-n", "--name", help="Branch name", type=str, default=None)

  cmd_stash = subparsers.add_parser("stash", help="Stash changes across worktrees")
  cmd_stash.set_defaults(func=stash)
  cmd_stash.add_argument("-n", "--no-untracked", help="Do not stash files", action="store_true")

  return args.parse_args()


GIT_BRANCH = proc("git rev-parse --abbrev-ref HEAD")

opts = parse_args()
opts.func(opts)
