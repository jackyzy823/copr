# Reference: https://github.com/fedora-copr/copr/blob/main/cli/man/copr-cli.1.asciidoc
# Prepare ~/.config/copr , install copr-cli
copr-cli buildscm --nowait --method make_srpm  --clone-url https://github.com/jackyzy823/copr --subdir <folder> --spec <spec-file> <copr-project>
