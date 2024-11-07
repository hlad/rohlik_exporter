{
  description = "Rohlik Prometheus Exporter Python development environment";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";
  };

  outputs = { self, nixpkgs, ... }@inputs:
    let
      system = "x86_64-linux";
      pkgs = import inputs.nixpkgs { inherit system; };
    in {
      devShells.x86_64-linux.default = pkgs.mkShell {
        nativeBuildInputs = with pkgs;
          let
            devpython = pkgs.python312.withPackages
              (ps: with ps; [ prometheus-client ]);
          in [ devpython ];
      };
    };
}