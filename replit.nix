{ pkgs }: {
  deps = [
    pkgs.python311Packages.pytest
    pkgs.python310Packages.pytest
  ];
}