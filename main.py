#!/usr/bin/env python3
"""Entry for make.fun news-image-20261117 (@agus-ite).

Copies the bundled front-page image (entry.png) to the output path.
The image itself is the entry: THE DAILY GLOBE, a newspaper front page
summing up the world news of Tuesday 17 November 2026 -- war in the Gulf,
the Kerch Bridge at night, aid for Gaza, the Shenzhen summit, and markets
in Manila.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    # Deterministic by construction: a byte-for-byte copy of the bundled
    # image, so both graded runs write identical output.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(os.path.join(HERE, "entry.png"),
                    os.path.join(out_dir, "entry.png"))


if __name__ == "__main__":
    main()
