default:
  @just --list

build:
  nix --extra-experimental-features flakes build .#default

run  +arguments:
  nix --extra-experimental-features flakes run .#default {{arguments}}

poetry +command:
  nix --extra-experimental-features flakes develop .#poetry  --command poetry {{command}}

flake +command:
  nix --extra-experimental-features flakes flake {{command}}
