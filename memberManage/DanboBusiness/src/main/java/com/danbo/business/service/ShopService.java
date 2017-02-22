package com.danbo.business.service;

import java.util.List;

import javax.annotation.Resource;

import org.springframework.stereotype.Service;

import com.danbo.business.dao.ShopDao;
import com.danbo.business.model.Image;
import com.danbo.business.model.ImageDetail;
import com.danbo.business.model.Shop;


@Service(value="shopService")
public class ShopService {
	@Resource(name="shopDao")
	private ShopDao shopDao;
	//增加购物车信息,购买后转为购物信息
	public String addGoods(Shop shop) {
		if(shopDao.addShop(shop)){
			return "success";
		}
		return "false";
	}
	
	//根据会员编号获得User实体类
	public List<Shop> findShopCartByLoginName(String loginname){
		List<Shop> listShops = shopDao.findShopByLoginName(loginname);
		return listShops;
	}
	
	//根据分类,获得商品图片信息
	public List<Image> findGoodsInfoByClassify(String classify){
		List<Image> listInfos = shopDao.findGoodsInfoByClassify(classify);
		return listInfos;
	}
	
    //根据上级图片id,找到图片详细信息 Image id 对应detailImage parentid
	public List<ImageDetail> findGoodsDetailByParentId(Integer id){
		List<ImageDetail> detailList = shopDao.findGoodsDetail(id);
		if(detailList.size() == 0){
			return null;
		}
		return detailList;
	}
	
	//根据图片地址,获得图片信息
	public List<Image> findGoodsInfoByUrl(String url){
		List<Image> imageList = shopDao.findGoodsInfoByurl(url);
		//查询结果不是一条,错误，		//查询一次  modCount +1 所以不能用为空判断
		if(imageList.size()>1 || imageList.size()==0){
			return null;
		}
		return imageList;
	}
	
	//删除购物车数据
	public boolean deleteShopCart(Integer id){
		return shopDao.deleteShopCart(id);
	}

	public ShopDao getShopDao() {
		return shopDao;
	}

	public void setShopDao(ShopDao shopDao) {
		this.shopDao = shopDao;
	}
}
