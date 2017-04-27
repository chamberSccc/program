package com.process.algor;

import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;

import javax.imageio.ImageIO;

import com.process.Utl.ImageBufferUtl;

public class GaussDifference extends ImageBufferUtl {
	
	public static void main(String args[]) throws IOException{
		String dateNowStr = creatImgName();
		BufferedImage src1 = ImageIO
				.read(new File("d:\\imginput\\test.jpg"));
		BufferedImage src2 = ImageIO
				.read(new File("d:\\imginput\\test.jpg"));
		GaussDifference gd = new GaussDifference();
		//这里开始运行高斯差分，设置参数
		BufferedImage out = gd.pretreatData(src1,src2, 0.6f, 4f, 2);
		ImageIO.write(out, "jpeg", new File("d:\\imginput\\" + dateNowStr
				+ "DOG.jpg"));
	}
	
	public BufferedImage pretreatData(BufferedImage src1,BufferedImage src2,float sigma1,float sigma2,int size) throws IOException{
		//先得到不同参数下的高斯卷积核
		float[][] gaussKernel1 = new float[2*size+1][2*size+1];
		float[][] gaussKernel2 = new float[2*size+1][2*size+1];
		float sum1,sum2;
		GaussKernel gk = new GaussKernel();
		gaussKernel1 = gk.getGaussKernelData2D(size, sigma1);
		sum1 = gk.getSumKernel(gaussKernel1, 2*size+1);
		gaussKernel2 = gk.getGaussKernelData2D(size, sigma2);
		sum2 = gk.getSumKernel(gaussKernel2, 2*size+1);
		
		//得到高斯模糊后的图
		GaussSmooth gs = new GaussSmooth();
		BufferedImage out1 = gs.smoothFilter(src1, gaussKernel1, sum1,size );
		//System.out.println("out1值1"+out1.getRGB(200, 210));
		BufferedImage out2 = gs.smoothFilter(src2, gaussKernel2, sum2, size);
		out1 = this.getDifferentGauss(out1, out2);
		return out1;
		
	}
	
	public BufferedImage getDifferentGauss(BufferedImage out1,BufferedImage out2){
		int tr1,tg1,tb1,tr2,tg2,tb2,subr,subg,subb;
		int width1 = out1.getWidth();
		int height1 = out1.getHeight();
		int width2 = out2.getWidth();
		int height2 = out2.getHeight();
		int[] imgPixel1 = new int[width1*height1];
		int[] imgPixel2 = new int[width2*height2];
		int[] outImgPexel = new int[width2*height2];
		getRGB(out1, 0, 0, width1, height1, imgPixel1);
		getRGB(out2, 0, 0, width2, height2, imgPixel2);
		for(int i=0;i<imgPixel1.length;i++){
			tr1 = (imgPixel1[i] >> 16) & 0xff;
			tg1 = (imgPixel1[i] >> 8) & 0xff;
			tb1 = imgPixel1[i] & 0xff;
			//System.out.println("tr1=" +tr1+" tg1=" +tg1+" tb1=" +tb1);
			tr2 = (imgPixel2[i] >> 16) & 0xff;
			tg2 = (imgPixel2[i] >> 8) & 0xff;
			tb2 = imgPixel2[i] & 0xff;
			//System.out.println("tr2=" +tr2+" tg2=" +tg2+" tb2=" +tb2);
			subr = tr1-tr2<0?0:tr1-tr2;
			subg = tg1-tg2<0?0:tg1-tg2;
			subb = tb1-tb2<0?0:tb1-tb2;
			//System.out.println("subr=" +subr+"subg=" +subr+"subb=" +subb);
			outImgPexel[i] = (255 << 24) | ( subr<< 16)
					| ( subg << 8) |  subb;
		}
		setRGB(out1, 0, 0, width1, height1, outImgPexel);
		return out1;
		
	}
	
}
