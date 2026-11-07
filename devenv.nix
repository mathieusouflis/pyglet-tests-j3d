{ pkgs, ... }:

{
  packages = [
    pkgs.git
    pkgs.ty
    pkgs.ruff
  ];

  languages.python = {
    enable = true;
    venv.enable = true;
    uv = {
      enable = true;
      sync.enable = true;
    };
  };
}
