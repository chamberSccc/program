package com.process.Utl;

import java.awt.image.BufferedImage;
import java.text.SimpleDateFormat;
import java.util.Date;

//图像处理工具
public class ImageBufferUtl {
	/**
	 * A convenience method for getting ARGB pixels from an image. This tries to
	 * avoid the performance penalty of BufferedImage.getRGB unmanaging the
	 * image.
	 */
	public int[] getRGB(BufferedImage image, int x, int y, int width,
			int height, int[] pixels) {
		int type = image.getType();
		if (type == BufferedImage.TYPE_INT_ARGB
				|| type == BufferedImage.TYPE_INT_RGB)
			return (int[]) image.getRaster().getDataElements(x, y, width,
					height, pixels);
		return image.getRGB(x, y, width, height, pixels, 0, width);
	}

	/**
	 * A convenience method for setting ARGB pixels in an image. This tries to
	 * avoid the performance penalty of BufferedImage.setRGB unmanaging the
	 * image.
	 */
	public void setRGB(BufferedImage image, int x, int y, int width,
			int height, int[] pixels) {
		int type = image.getType();
		if (type == BufferedImage.TYPE_INT_ARGB
				|| type == BufferedImage.TYPE_INT_RGB)
			image.getRaster().setDataElements(x, y, width, height, pixels);
		else
			image.setRGB(x, y, width, height, pixels, 0, width);
	}

	// 给输出图片唯一命名
	public static String creatImgName() {
		Date d = new Date();
		SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
		String dateNowStr = sdf.format(d).trim().replace("-", "")
				.replace(":", "");
		return dateNowStr;
	}
}
