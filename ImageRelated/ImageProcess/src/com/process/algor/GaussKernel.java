package com.process.algor;
/*
 * @Purpose 产生高斯核用于卷积
 * @Dimensionality 二维
 * @User ChenBo
 * @Time 2016.12.22
 * 
 * @Param sigma 标准差
 * @Param n 模糊半径
 */
public class GaussKernel {
	int size = 0;
	public float[][] getGaussKernelData2D(int n,float sigma){
		size = 2*n +1;
		float sigma22 = 2*sigma*sigma;
		float sigma22PI = (float) (Math.PI * sigma22);
		float[][] kernelData = new float[size][size];
		int row = 0;
		for(int i=-n;i<=n;i++){
			int column = 0;
			for(int j=-n;j<=n;j++){
				float xDistance = i*i;
				float yDistance = j*j;
				kernelData[row][column] = (float) Math.exp(-(xDistance+yDistance)/sigma22)/sigma22PI;
				column++;
			}
			row++;
		}
		for(int i=0;i<size;i++){			
			for(int j=0;j<size;j++){
				System.out.print("\t" + kernelData[i][j]); 
			}
			System.out.println();  
	        System.out.println("\t ---------------------------"); 
		}
		return kernelData;		
	}
	//方便归一化处理，先得到核矩阵的总和
	public float getSumKernel(float[][] kernel,int size){
		float sum =(float) 0.0;
		for(int i=0;i<size;i++){			
			for(int j=0;j<size;j++){
				sum+= kernel[i][j];
			}
		}
		//System.out.println(sum);
		return sum;

	}
	
}
