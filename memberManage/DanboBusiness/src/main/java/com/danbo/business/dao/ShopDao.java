package com.danbo.business.dao;

import java.util.ArrayList;
import java.util.List;

import javax.annotation.Resource;
import javax.persistence.criteria.From;

import org.springframework.dao.DataAccessException;
import org.springframework.orm.hibernate4.HibernateTemplate;
import org.springframework.stereotype.Repository;

import com.danbo.business.model.Image;
import com.danbo.business.model.Shop;
import com.danbo.business.model.ImageDetail;



@Repository(value="shopDao")
public class ShopDao {
	@Resource(name="hibernateTemplate")
	private HibernateTemplate hibernateTemplate;
	//添加购物信息
	public boolean addShop(Shop shop) {
	   try {
		    hibernateTemplate.save(shop);   
			} catch (Exception e) {
	           return false;			
			}
	   return true;
	}
	//根据会员编号查询,获得购物车信息
	@SuppressWarnings("unchecked")
	public  List<Shop> findShopByLoginName(String loginname) {
			List<Shop> shopList = new ArrayList<Shop>();
			String queryString = "from Shop where loginname =:loginname and state = '未购买'";
			shopList = (List<Shop>) hibernateTemplate.findByNamedParam(queryString,"loginname",loginname);
	        return shopList;
	}	
	
	//根据图片分类查询,获得商品图片信息
	@SuppressWarnings("unchecked")
	public  List<Image> findGoodsInfoByClassify(String classify) {
			List<Image> infoList = new ArrayList<Image>();
			String queryString = "from Image where classify =:classify";
			infoList = (List<Image>) hibernateTemplate.findByNamedParam(queryString,"classify",classify);
		    return infoList;
	}

	//根据图片地址,获得图片信息
	@SuppressWarnings("unchecked")
	public  List<Image> findGoodsInfoByurl(String url) {
			List<Image> infoList = new ArrayList<Image>();
			String queryString = "from Image where url =:url";
			infoList = (List<Image>) hibernateTemplate.findByNamedParam(queryString,"url",url);
		    return infoList;
	}
	
	//根据上级图片id,找到图片详细信息 Image id 对应detailImage parentid
	@SuppressWarnings("unchecked")
	public List<ImageDetail> findGoodsDetail(Integer id){
		   List<ImageDetail> detailList = new ArrayList<ImageDetail>();
		   String queryString ="from ImageDetail where parentid = :parentid";
		   detailList = (List<ImageDetail>) hibernateTemplate.findByNamedParam(queryString,"parentid",id);
		   return detailList;
	}
	
	//删除购物车信息
	public boolean deleteShopCart(Integer id){
		try {
			Shop shop = hibernateTemplate.get(Shop.class, id);
			hibernateTemplate.delete(shop);
		} catch (Exception e) {
			return false;
		}
		return true;
	}		
}
