import datetime
from pathlib import Path

import numpy as np
import pyperclip
import pyvips
import typer
from PIL import Image, ImageGrab

app = typer.Typer()


@app.command()
def main():
    """
    クリップボード内の画像をwebpに変換しカレントディレクトリ/images/に保存し
    md記法で画像リンクのテキストをクリップボードに保存します
    """
    img = get_clipboard_image()

    if img is None:
        typer.echo("not image")
        return

    ts = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
    filepath = Path("image") / f"{ts}.webp"

    save_image(
        convert(pil_to_vips(img)),
        filepath
    )

    md = f"![screen shot]({filepath})"
    pyperclip.copy(md)


def save_image(img: pyvips.Image, filepath: Path):
    """
    filepathの親フォルダがない場合作成し、imgを保存
    """
    filepath.parent.mkdir(exist_ok=True)
    img.webpsave(filepath, lossless=True)



def get_clipboard_image() -> Image.Image | None:
    """
    クリップボードから画像を取得
    """
    img = ImageGrab.grabclipboard()

    match img:
        case Image.Image() as img:
            return img
        case _:
            return None


def pil_to_vips(img: Image.Image) -> pyvips.Image:
    """
    PILのImageをpyvips.Imageに変換
    """
    arr = np.asarray(img.convert("RGBA"))

    return pyvips.Image.new_from_memory(
        arr.tobytes(), arr.shape[1], arr.shape[0], 4, "uchar"
    )


def convert(img: pyvips.Image) -> pyvips.Image:
    return img.resize(0.5, kernel="lanczos3")
