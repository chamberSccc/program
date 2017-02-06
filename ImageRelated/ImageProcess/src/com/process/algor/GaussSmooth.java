package com.process.algor;

import java.awt.Color;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Date;

import javax.imageio.ImageIO;

import com.process.Utl.ImageBufferUtl;

public class GaussSmooth extends ImageBufferUtl{

	public static void main(String[] args)  throws IOException{
		String dateNowStr = creatImgName();
	    int size = 2;
		int matSize = size*2+1;//卷积核矩阵大小
		BufferedImage img = ImageIO.read(new File("d:\\imginput\\test.jpg"));
		//用于做卷积的矩阵
		float[][] kernelMatrix = new float [matSize][matSize];
		//float[][] kernelMatrix = {{1,2,3},{2,3,4},{1,3,4}};
		//先计算高斯卷积核矩阵
		GaussKernel gk = new GaussKernel();
		kernelMatrix = gk.getGaussKernelData2D(size, 1f);
		float sum = gk.getSumKernel(kernelMatrix, matSize);
		GaussSmooth gs = new GaussSmooth();
		BufferedImage out = gs.smoothFilter(img, kernelMatrix, sum, size);		
		ImageIO.write(out, "jpeg", new File("d:\\imginput\\"+dateNowStr+"SMOOTH.jpg"));
	}
	
	public BufferedImage smoothFilter(BufferedImage src,float[][] GaussKernel,float kernelSum,int size) {
		int width = src.getWidth();
		int height = src.getHeight();
		int[] inPixels = new int[width * height];
		int[] outPixels = new int[width * height];
		getRGB(src, 0, 0, width, height, inPixels);
		// 每一行、每一列的循环每个像素,index为当前处理点的索引，converIndex为卷积时3x3矩阵索引
		int index = 0, converIndex = 0;
		//x、y方向的RGB
		float rf= 0, gf = 0, bf = 0;
		int   ri= 0, gi = 0, bi = 0;
		int converRow, converCol;
		for (int row = 0; row < height; row++) {
			int ta = 255, tr = 0, tg = 0, tb = 0;
			for (int col = 0; col < width; col++) {
				index = row * width + col;
				for (int subrow = -size; subrow <= size; subrow++) {
					for (int subcol = -size; subcol <= size; subcol++) {
						//converRow代表图像被卷积部分的当前行
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

						rf += (GaussKernel[subrow + size][subcol + size] * tr);
						gf += (GaussKernel[subrow + size][subcol + size] * tg);
						bf += (GaussKernel[subrow + size][subcol + size] * tb);

					}
				}
				//加权平均后,进行归一化
		        //加权平均和得到后，进行归一化
		        rf = rf/kernelSum;
		        gf = gf/kernelSum;
		        bf = bf/kernelSum;
				outPixels[index] = (ta << 24) | (dealThresh((int) rf) << 16)
						| (dealThresh((int) gf) << 8) | dealThresh((int) bf);
				converRow = converCol = 0;
				rf = gf = bf = 0;
				ri = gi = bi = 0;

			}
		}
		
		setRGB(src, 0, 0, width, height, outPixels);
		return src;
	}

	public static int dealThresh(int value) {
		return value < 0 ? 0 : (value > 255 ? 255 : value);
	}
	
	
}
