package com.process.algor;

import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import java.text.DecimalFormat;

import javax.imageio.ImageIO;
/*
 * chenbo
 * 2017.01.18
 */

import com.process.Utl.ImageBufferUtl;

public class ImageCompress extends ImageBufferUtl {
	public static void main(String[] args)  throws IOException{
		//double[] a = {34,34,34,33,34,28,35,32,34,34,34,33,34,28,35,32,34,34,34,33,34,28,35,32,34,34,34,33,34,28,35,32,34,34,34,33,34,28,35,32,36,36,29,27,33,31,30,31,32,32,35,30,32,33,31,27,30,30,27,28,30,30,28,29};
		ImageCompress ic = new ImageCompress();
		ic.sortByZigzag();
	}
	//��׼���ȡ�ɫ����������,
	public double[] YStandardMatrix = {16,11,10,16,24,40,51,61,12,12,14,19,26,58,60,55,14,13,16,24,40,57,69,56,
									   14,17,22,29,51,87,80,62,18,22,37,56,68,109,103,77,24,35,55,64,81,104,113,
									   92,49,64,78,87,103,121,120,101,72,92,95,98,112,100,103,99};
	public double[] CStandardMatrix = {17,18,24,47,99,99,99,99,18,21,26,66,99,99,99,99,24,26,56,99,99,99,99,99,
									   47,66,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,
									   99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99};
	//Y����  Crɫ�� Cb���Ͷ� DCTֻ�ܴ���8x8����
	public double[] YMatrix;
	public double[] CrMatrix;
	public double[] CbMatrix;
	public double[] DctYMatrix;
	public double[] DctCrMatrix;
	public double[] DctCbMatrix;
	//�洢����֮�����������
	//public int[][] quanYMatrix = {{1,2,3,4},{5,6,7,8},{9,10,11,12},{13,14,15,16}};
	public int[][] quanYMatrix  = new int[8][8];
	public int[][] quanCrMatrix = new int[8][8];
	public int[][] quanCbMatrix = new int[8][8];
	//�洢����֮��,������й���������ĵ���������
	public int[] hufYMatrix = new int[64];
	public int[] hufCrMatrix = new int[64];
	public int[] hufCbMatrix = new int[64];
	
	//ԭʼRGB����ת��Ϊ����Y��Cr��Cb�����飬�������ת��Ϊ���󲻹�8x8�ֿ飬��ֻ���ͼ�����飬����Ŀճ���
	public void separateMatrix(BufferedImage src){
		int width = src.getWidth();
		int height = src.getHeight();
		int newWidth = 0;
		int newHeight =0;
		if(width%8 != 0)
			newWidth = width+8-width%8;
		if(height%8 != 0)
			newHeight = height+8-height%8;
		int[] pixels = new int[width * height];
		getRGB(src, 0, 0, width, height, pixels);
		YMatrix  = new double[newWidth*newHeight];
		CrMatrix = new double[newWidth*newHeight];
		CbMatrix = new double[newWidth*newHeight];
		int  tR = 0, tG = 0, tB = 0;
		for(int i=0;i<pixels.length;i++){
			tR = (pixels[i] >> 16) & 0xff;
			tG = (pixels[i] >> 8) & 0xff;
			tB = pixels[i] & 0xff;
			YMatrix[i] = tR*0.299+0.587*tG+0.114*tB;
			CrMatrix[i]= -0.1687*tR-0.3313*tG+0.5*tB;
			CbMatrix[i]= tR*0.5-0.4187*tG-0.0813*tB;
		}
	}
	
	//��ɢ����ת��
	public void DCT(int width,int height){
		DecimalFormat df=new DecimalFormat("#.00");
		DctYMatrix = new double[64];
		DctCrMatrix = new double[64];
		DctCbMatrix = new double[64];
		for(int i=0;i<width/8;i++){
			for(int j=0;j<height/8;j++){
				//8x8������к��� u,v
				for(int u=0;u<8;u++){
					for(int v=0;v<8;v++){
						double tempY = 0, tempCr =0, tempCb =0;
						//x yΪ��ʽ���ۼӷ���
						for(int x=0;x<8;x++){
							for(int y=0;y<8;y++){
								int index1 = i*width*8+8*j+x*width+y;
								tempY += alpha(u,v)*YMatrix[index1]*Math.cos((u*Math.PI*(2*x+1))/16)*Math.cos((v*Math.PI*(2*y+1))/16);
								tempCr += alpha(u,v)*CrMatrix[index1]*Math.cos((u*Math.PI*(2*x+1))/16)*Math.cos((v*Math.PI*(2*y+1))/16);
								tempCb += alpha(u,v)*CbMatrix[index1]*Math.cos((u*Math.PI*(2*x+1))/16)*Math.cos((v*Math.PI*(2*y+1))/16);
/*								if(u==0 && v==1){
									System.out.println("a1="+a1+"   a2="+a2+"   a3="+a3+"   a5="+a5);
								}*/
							}
						}
						//һά�����±��ά����λ�ù�ϵ
						int index2 = i*width*8+8*j+u*width+v;
						DctYMatrix[index2] = Double.parseDouble(df.format(tempY))==-0.0? 0:Double.parseDouble(df.format(tempY));
						DctCrMatrix[index2] = Double.parseDouble(df.format(tempCr))==-0.0? 0:Double.parseDouble(df.format(tempCr));
						DctCbMatrix[index2] = Double.parseDouble(df.format(tempCb))==-0.0? 0:Double.parseDouble(df.format(tempCb));
					}
				}
			}
		}
		
	}
	
	//��������
	public void dataQuantification(){
		for(int i=0;i<8;i++){
			for(int j=0;j<8;j++){
				quanYMatrix[i][j] = (int) Math.round(DctYMatrix[i*8+j]/YStandardMatrix[i*8+j]);
				quanCrMatrix[i][j] = (int) Math.round(DctCrMatrix[i*8+j]/CStandardMatrix[i*8+j]);
				quanCbMatrix[i][j] = (int) Math.round(DctCbMatrix[i*8+j]/CStandardMatrix[i*8+j]);	
			}
		}
	}
	
	//zigzag����
	public void sortByZigzag(){
		int size = quanYMatrix.length;
		int x=0,y=0;
		for(int i=0;i<size;i++){
			for(int j=0;j<size;j++){
				hufYMatrix[i*size+j]  = quanYMatrix[x][y];
				hufCbMatrix[i*size+j]  = quanCbMatrix[x][y];
				hufCrMatrix[i*size+j]  = quanCrMatrix[x][y];
				//�α귽������
				if(y%2==0 && y!=size-1 && (x==0 || x==size-1)){
					y++;
					continue;
				}
				//����
			    if(x%2==1 && x!=size-1 && (y==0 || y==size-1)){
					x++;
					continue;
				}
				//���Ͻ�
				if((x+y)%2==0 && y!=size-1 && x!=0){
					x--;
					y++;
					continue;
				}
				//���½�
				else if((x+y)%2==1){
					x++;
					y--;
					continue;
				}else{
					continue;
				}
			}
		}
	}
	
	
	public double alpha(int u,int v){
		if(u==0 && v==0){
			return 0.125;
		}else if(u==0 && v!=0){
			return 0.5*(1/Math.sqrt(8));
		}else if(u!=0 && v==0){
			return 0.5*(1/Math.sqrt(8));
		}else{
			return 0.25;
		}
	}
}
