# Focus — Pinterest 参考复刻

参考：用户提供的 Pinterest.mp4（Eagle ID MUKRCUY5R8SV6）。原画幅 702×494，30fps，18秒／540帧。完整参考分析见 ANALYSIS.md。

## 文件

- out/Replica.mp4：参考复刻版，保留用户视频原音轨。
- out/Motion.mp4：同版时序的纯动效，替换文字、照片、材质及配色，静音。
- src/index.tsx：共享运动组件、场景切换表和各 Composition。

## 运行

Node.js、Python 3（numpy、Pillow）、ffmpeg；系统字体 Times New Roman、Arial Black 和 Apple SD Gothic Neo（在本机 macOS 验证）。

```sh
npm ci
python3 -m pip install numpy Pillow
npm run studio
npm run render
npm run render:motion
```

Studio 入口 Replica / Motion。离线渲染使用 ReplicaSamples / MotionSamples，以 90fps 输出3子帧，再合成为30fps；快门偏移为 -0.3/0/+0.3 个输出帧，跨度0.6帧。没有以整屏静态模糊代替运动曝光。硬切边界可能保留曝光跨帧混合。

## 可编辑范围

所有文字、位置、旋转、环形排列、文件夹、字母圆点和时序是源码层参数；修改 Content() 的时间区间和相应组件。只有 neutral / samples 是实际接入的 props，不支持任意内容数量或任意时长自动适配。纯动效使用相同运动路径，字符单元变为几何块；这不是对成片去色。

public 中仅四个参考照片缩略图及提取音轨来自用户视频。未将完整原视频嵌入成片。金属罐、键帽、棋子、柠檬为程序化或字形近似；没有恢复原片3D模型、原字体文件或源工程关键帧。韩文手写字形由本地字体近似。原片署名/声明作为参考内容保留，不代表本工程作者署名。

本工程是独立参考研究版本，未修改已交付资产、未入本地资产库。当前仅原画幅，不声称已完成横竖屏适配或逐像素一致。未进行音素级对齐。

可选环境变量 `RENDER_OUTPUT_DIR` 指定子帧与成片输出目录；默认 `out`。用于新发布渲染时保存独立版本，不覆盖先前交付。发布示例：`RENDER_OUTPUT_DIR=out/publish-v1 npm run render`。

## 社区发布

[Motion Face 视频](https://motionface.cc/?recording=8b292133-ec1f-46dc-aea7-3da4319c76e5)

发布成片由本工程 `Replica` 的三子帧管线生成，18秒、702×494、30fps。仓库不含渲染产物；`public/` 为工程运行所需的参考照片裁片及原音轨。
