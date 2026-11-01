# -*- coding: utf-8 -*-
"""Build A3/A2 Beijing control-plan 图则 layout shells with PyQGIS.

The templates are layout shells: map frames, title bar, legend, locator,
inset frames and an indicator-table placeholder. They contain no project data.
"""
from __future__ import annotations

import pathlib

from qgis.core import (
    QgsApplication,
    QgsProject,
    QgsPrintLayout,
    QgsLayoutPoint,
    QgsLayoutSize,
    QgsLayoutItemMap,
    QgsLayoutItemLabel,
    QgsLayoutItemShape,
    QgsLayoutItemScaleBar,
    QgsLayoutExporter,
    QgsLayoutMeasurement,
    QgsUnitTypes,
    QgsFillSymbol,
    QgsRectangle,
    QgsCoordinateReferenceSystem,
    QgsReadWriteContext,
)
from qgis.PyQt.QtGui import QColor, QFont
from qgis.PyQt.QtCore import Qt

BASE = pathlib.Path(__file__).resolve().parent.parent
OUT = BASE / "templates" / "beijing"
PREVIEW = OUT / "previews"
OUT.mkdir(parents=True, exist_ok=True)
PREVIEW.mkdir(parents=True, exist_ok=True)

INK = "#1d2524"
MUTED = "#5f6b68"
LINE = "#2b3331"
PAPER = "#ffffff"
MAP_BG = "#fafaf7"
FONT = "Microsoft YaHei"


def add_rect(layout, x, y, w, h, fill="255,255,255,0", stroke=LINE, width=0.25):
    item = QgsLayoutItemShape(layout)
    layout.addLayoutItem(item)
    item.setShapeType(QgsLayoutItemShape.Shape.Rectangle)
    item.attemptMove(QgsLayoutPoint(x, y))
    item.attemptResize(QgsLayoutSize(w, h))
    item.setSymbol(QgsFillSymbol.createSimple({
        "color": fill,
        "outline_color": stroke,
        "outline_width": str(width),
    }))
    return item


def add_text(layout, x, y, w, h, text, size=6.0, bold=False,
             color=INK, align=Qt.AlignmentFlag.AlignLeft, valign=Qt.AlignmentFlag.AlignVCenter):
    item = QgsLayoutItemLabel(layout)
    layout.addLayoutItem(item)
    item.setText(text)
    font = QFont(FONT)
    font.setPointSizeF(size)
    font.setBold(bold)
    item.setFont(font)
    item.setFontColor(QColor(color))
    item.setHAlign(align)
    item.setVAlign(valign)
    item.attemptMove(QgsLayoutPoint(x, y))
    item.attemptResize(QgsLayoutSize(w, h))
    return item


def add_map(layout, x, y, w, h, label, label_size=9.0):
    add_rect(layout, x, y, w, h, "255,255,255,255", LINE, 0.3)
    m = QgsLayoutItemMap(layout)
    layout.addLayoutItem(m)
    m.attemptMove(QgsLayoutPoint(x + 0.5, y + 0.5))
    m.attemptResize(QgsLayoutSize(w - 1.0, h - 1.0))
    m.setFixedSize(QgsLayoutSize(w - 1.0, h - 1.0))
    m.setFrameEnabled(False)
    m.setBackgroundColor(QColor(MAP_BG))
    m.setCrs(QgsCoordinateReferenceSystem("EPSG:3857"))
    m.setExtent(QgsRectangle(0, 0, 1000, 1000))
    m.setScale(10000)
    add_text(layout, x + 4, y + h / 2 - 5, w - 8, 10, label, label_size,
             False, MUTED, Qt.AlignmentFlag.AlignHCenter)
    return m


def add_scale_bar(layout, x, y, w, h, map_item=None):
    """Visible placeholder scale bar; replace with a linked QGIS scale bar later."""
    add_text(layout, x, y, w, 4, "示意比例尺（替换）", 4.8, False, MUTED)
    seg_w = w / 4.0
    for i in range(4):
        color = "35,42,40,255" if i % 2 == 0 else "255,255,255,255"
        add_rect(layout, x + i * seg_w, y + 5.0, seg_w, 2.4, color, LINE, 0.15)
    for i, label in enumerate(("0", "50", "100", "200 m")):
        add_text(layout, x + i * seg_w - 3, y + 7.8, 10, 4, label, 4.8, False, MUTED,
                 Qt.AlignmentFlag.AlignHCenter)


def add_north(layout, x, y):
    add_text(layout, x, y, 10, 5, "N", 9, True, INK, Qt.AlignmentFlag.AlignHCenter)
    add_text(layout, x, y + 4.5, 10, 8, "▲", 11, True, INK, Qt.AlignmentFlag.AlignHCenter)


def add_legend(layout, x, y, w, h):
    add_rect(layout, x, y, w, h, "255,255,255,255", LINE, 0.25)
    add_text(layout, x + 3, y + 1.5, w - 6, 5, "图 例", 8.0, True)
    items = [
        ("街区边界", "line", "#c0392b"),
        ("城市干路", "line", "#727b78"),
        ("城市支路", "line", "#9aa29f"),
        ("河道上口线", "line", "#2f6f8f"),
        ("绿色空间", "fill", "#49b84e"),
        ("水域", "fill", "#a9d6ea"),
        ("公共服务设施", "point", "#f0c419"),
        ("城市安全设施", "point", "#e67e22"),
        ("交通设施", "point", "#2e86c1"),
        ("市政设施", "point", "#8e44ad"),
    ]
    y0 = y + 7.0
    step = min(5.4, (h - 9.0) / len(items))
    for i, (name, kind, color) in enumerate(items):
        yy = y0 + i * step
        if kind == "line":
            add_rect(layout, x + 3, yy + 1.8, 10, 0.7, color, color, 0.0)
        elif kind == "fill":
            add_rect(layout, x + 3, yy + 0.7, 10, 4.0, color, color, 0.0)
        else:
            add_rect(layout, x + 5, yy + 1.0, 4, 4, color, color, 0.0)
        add_text(layout, x + 16, yy, w - 19, 5.0, name, 5.1, False, INK)


def add_table(layout, x, y, w, h):
    add_rect(layout, x, y, w, h, "255,255,255,255", LINE, 0.25)
    headers = ["地块编号", "用地性质", "面积(ha)", "容积率", "高度(m)", "备注"]
    widths = [24, 34, 24, 20, 24, 84]
    header_h = 8.0
    row_h = 8.0
    add_rect(layout, x, y, w, header_h, "236,239,236,255", LINE, 0.2)
    cx = x
    for head, cw in zip(headers, widths):
        add_text(layout, cx + 0.8, y + 0.5, cw - 1.6, header_h - 1, head, 5.0, True,
                 INK, Qt.AlignmentFlag.AlignHCenter)
        cx += cw
    for r in range(4):
        yy = y + header_h + r * row_h
        add_rect(layout, x, yy, w, row_h, "255,255,255,0", LINE, 0.12)
        cx = x
        for cw in widths:
            add_rect(layout, cx, yy, 0.0, row_h, "255,255,255,0", LINE, 0.12)
            add_text(layout, cx + 0.8, yy, cw - 1.6, row_h, "—", 5.0, False, MUTED,
                     Qt.AlignmentFlag.AlignHCenter)
            cx += cw
    add_text(layout, x + 1, y + header_h + 4 * row_h, w - 2, h - header_h - 4 * row_h,
             "示意表头；接入项目数据后替换。", 4.8, False, MUTED)


def add_title_bar(layout, W, H, M, title_h, sheet_no):
    add_rect(layout, M, M, W - 2 * M, H - 2 * M, "255,255,255,0", LINE, 0.55)
    add_rect(layout, M + 2, M + 2, W - 2 * M - 4, H - 2 * M - 4, "255,255,255,0", LINE, 0.22)
    add_rect(layout, M + 2, M + 2, W - 2 * M - 4, title_h, "255,255,255,255", LINE, 0.3)
    add_text(layout, M + 5, M + 3.5, W * 0.52, 9, "项目名称（替换）", 12.5, True)
    add_text(layout, M + 5, M + title_h - 7, W * 0.52, 5.5,
             "控制性详细规划（街区层面）图则 · 模板", 6.5, False, MUTED)
    add_text(layout, W - M - 92, M + 3, 70, 8, "控制图则", 11.5, True, INK,
             Qt.AlignmentFlag.AlignHCenter)
    add_text(layout, W - M - 24, M + 3, 18, 8, sheet_no, 8.5, True, INK,
             Qt.AlignmentFlag.AlignHCenter)
    add_text(layout, W - M - 92, M + title_h - 7, 86, 5, "图则编号 / 比例待填", 5.8, False,
             MUTED, Qt.AlignmentFlag.AlignHCenter)


def add_footer(layout, W, H, M, text):
    add_text(layout, M + 1, H - M + 1.2, W - 2 * M - 2, 4.5, text, 5.0, False, MUTED)


def build_a3(project):
    layout = QgsPrintLayout(project)
    layout.initializeDefaults()
    layout.setName("A3 北京控规图则")
    W, H, M = 420.0, 297.0, 8.0
    page = layout.pageCollection().page(0)
    page.setPageSize(QgsLayoutSize(W, H, QgsUnitTypes.LayoutMillimeters))
    add_title_bar(layout, W, H, M, 20.0, "01")
    main = add_map(layout, M, 30, 250, 256, "主图（替换为项目地图）", 11.0)
    add_scale_bar(layout, 270, 101, 70, 9, main)
    add_north(layout, 402, 100)
    add_map(layout, 264, 32, 148, 46, "项目位置示意图", 7.0)
    add_legend(layout, 264, 118, 148, 64)
    add_map(layout, 264, 184, 148, 32, "附图 1（主导功能）", 6.5)
    add_map(layout, 264, 218, 148, 32, "附图 2（基准强度）", 6.5)
    add_map(layout, 264, 252, 148, 36, "附图 3（基准高度）", 6.5)
    add_footer(layout, W, H, M,
               "编制单位：________    日期：________    依据：________（待填）    图号：01")
    return layout


def build_a2(project):
    layout = QgsPrintLayout(project)
    layout.initializeDefaults()
    layout.setName("A2 北京控规图则")
    W, H, M = 594.0, 420.0, 10.0
    page = layout.pageCollection().page(0)
    page.setPageSize(QgsLayoutSize(W, H, QgsUnitTypes.LayoutMillimeters))
    add_title_bar(layout, W, H, M, 26.0, "01")
    main = add_map(layout, M, 40, 356, 366, "主图（替换为项目地图）", 13.0)
    add_scale_bar(layout, 386, 116, 90, 10, main)
    add_north(layout, 572, 115)
    add_map(layout, 374, 40, 210, 60, "项目位置示意图", 8.0)
    add_legend(layout, 374, 150, 210, 64)
    add_map(layout, 374, 218, 210, 42, "附图 1（主导功能）", 7.0)
    add_map(layout, 374, 264, 210, 42, "附图 2（基准强度）", 7.0)
    add_map(layout, 374, 310, 210, 42, "附图 3（基准高度）", 7.0)
    add_table(layout, 374, 356, 210, 50)
    add_footer(layout, W, H, M,
               "编制单位：________    日期：________    依据：________（待填）    图号：01")
    return layout


def export_pdf(layout, path, dpi=150):
    exporter = QgsLayoutExporter(layout)
    settings = QgsLayoutExporter.PdfExportSettings()
    settings.dpi = dpi
    return exporter.exportToPdf(str(path), settings)


def main():
    qgs = QgsApplication([], False)
    qgs.initQgis()
    project = QgsProject.instance()
    project.clear()
    layouts = [build_a3(project), build_a2(project)]
    for layout in layouts:
        safe = "A3" if "A3" in layout.name() else "A2"
        qpt = OUT / f"{safe}_beijing_control_tuze.qpt"
        pdf = PREVIEW / f"{safe}_beijing_control_tuze.pdf"
        layout.saveAsTemplate(str(qpt), QgsReadWriteContext())
        result = export_pdf(layout, pdf)
        print(safe, "qpt", qpt.exists(), qpt.stat().st_size if qpt.exists() else 0,
              "pdf", result, pdf.exists(), pdf.stat().st_size if pdf.exists() else 0)
    qgs.exitQgis()


if __name__ == "__main__":
    main()
