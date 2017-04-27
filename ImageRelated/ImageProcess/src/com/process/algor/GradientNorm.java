package com.process.algor;

import java.awt.Color;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import java.text.SimpleDateFormat;
import java.util.Date;

import javax.imageio.ImageIO;

import com.process.Utl.ImageBufferUtl;

public class GradientNorm extends ImageBufferUtl{

	public static void main(String[] args) throws IOException {
		String dateNowStr = creatImgName();
		GradientNorm gd = new GradientNorm();
		BufferedImage img = ImageIO
				.read(new File("d:\\imginput\\test.jpg"));
		BufferedImage out = gd.gradientFilter(img);
		ImageIO.write(img, "jpeg", new File("d:\\imginput\\" + dateNowStr
				+ "GRAD.jpg"));
	}
	// sobel算子
	public final static int[][] SOBEL_X = new int[][] { { -1, 0, 1 },
			{ -2, 0, 2 }, { -1, 0, 1 } };
	public final static int[][] SOBEL_Y = new int[][] { { -1, -2, -1 },
			{ 0, 0, 0 }, { 1, 2, 1 } };

	public BufferedImage gradientFilter(BufferedImage src) {
		int width = src.getWidth();
		int height = src.getHeight();
		int[] inPixels = new int[width * height];
		int[] outPixels = new int[width * height];
		getRGB(src, 0, 0, width, height, inPixels);
		// 每一行、每一列的循环每个像素,index为当前处理点的索引，converIndex为卷积时3x3矩阵索引
		int index = 0, converIndex = 0;
		//x、y方向的RGB
		double xr = 0, xg = 0, xb = 0; double yr = 0, yg = 0, yb = 0;
		int converRow, converCol;
		for (int row = 0; row < height; row++) {
			int ta = 255, tr = 0, tg = 0, tb = 0;
			for (int col = 0; col < width; col++) {
				index = row * width + col;
				for (int subrow = -1; subrow <= 1; subrow++) {
					for (int subcol = -1; subcol <= 1; subcol++) {
						//newRow代表当前卷积3X3矩阵的当前行
						converRow = row + subrow;
						converCol = col + subcol;
						if (converRow < 0 || converRow >= height) {
							converRow = row;
						}
						if (converCol < 0 || converCol >= width) {
							converCol = col;
						}
						converIndex = converRow * width + converCol;
						tr = (inPixels[converIndex] >> 16) & 0xff;
						tg = (inPixels[converIndex] >> 8) & 0xff;
						tb = inPixels[converIndex] & 0xff;

						xr += (SOBEL_X[subrow + 1][subcol + 1] * tr);
						xg += (SOBEL_X[subrow + 1][subcol + 1] * tg);
						xb += (SOBEL_X[subrow + 1][subcol + 1] * tb);

						yr += (SOBEL_Y[subrow + 1][subcol + 1] * tr);
						yg += (SOBEL_Y[subrow + 1][subcol + 1] * tg);
						yb += (SOBEL_Y[subrow + 1][subcol + 1] * tb);

					}
				}
				//xy方向梯度（振幅）
				double mred = Math.sqrt(xr * xr + yr * yr);
				double mgreen = Math.sqrt(xg * xg + yg * yg);
				double mblue = Math.sqrt(xb * xb + yb * yb);
				outPixels[index] = (ta << 24) | (dealThresh((int) mred) << 16)
						| (dealThresh((int) mgreen) << 8) | dealThresh((int) mblue);

				converRow = converCol = 0;
				xr = xg = xb = 0;
				yr = yg = yb = 0;

			}
		}
		setRGB(src, 0, 0, width, height, outPixels);
		return src;
	}

	public static int dealThresh(int value) {
		return value < 0 ? 0 : (value > 255 ? 255 : value);
	}
}
