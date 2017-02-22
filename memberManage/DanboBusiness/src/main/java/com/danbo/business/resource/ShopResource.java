package com.danbo.business.resource;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

import javax.annotation.Resource;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpSession;
import javax.ws.rs.Consumes;
import javax.ws.rs.GET;
import javax.ws.rs.POST;
import javax.ws.rs.Path;
import javax.ws.rs.PathParam;
import javax.ws.rs.Produces;
import javax.ws.rs.core.Context;
import javax.ws.rs.core.MediaType;

import org.springframework.context.annotation.Scope;
import org.springframework.stereotype.Component;

import com.danbo.business.model.Image;
import com.danbo.business.model.ImageDetail;
import com.danbo.business.model.Shop;
import com.danbo.business.service.ShopService;

import net.sf.json.JSON;
import net.sf.json.JSONObject;

@Component
@Path("/shop")
@Scope("prototype")
public class ShopResource {
	@Resource(name="shopService")
	private ShopService shopService;
	private String message;
	
	@POST
	@Path("/addShop")
	@Consumes(MediaType.APPLICATION_JSON)
	@Produces(MediaType.APPLICATION_JSON)
	//添加商品到购物车
	public String addShop(Shop shop,@Context HttpServletRequest request) {
		String loginname = "";
		HttpSession session = request.getSession(false); 
	    if(session != null){  
	    	Object sessionObj =  session.getAttribute("loginname");   
	    	loginname = (String) sessionObj;
	     } else{
	    	 return "false";
	     }
	    shop.setLoginname(loginname);
		String message = shopService.addGoods(shop);
		JSONObject jsonObject = new JSONObject();
		jsonObject.put("message", message);
		return jsonObject.toString();
	}

	@GET
	@Path("/getShopCart")
	@Consumes(MediaType.APPLICATION_JSON)
	@Produces(MediaType.APPLICATION_JSON)
	//查询购物车列表
	public String getShopCart(@Context HttpServletRequest request) {
		String loginname = "";
		HttpSession session = request.getSession(false); 
	    if(session != null){  
	    	Object sessionObj =  session.getAttribute("loginname");   
	    	loginname = (String) sessionObj;
	      } 
	    List<Shop> shopList = shopService.findShopCartByLoginName(loginname); 
	    Map map = new HashMap();
        map.put("aaData", shopList);
		JSONObject jsonUser = JSONObject.fromObject(map);
		return jsonUser.toString();
	}
	
	@GET
	@Path("/getGoodsInfo/{classify}")
	@Consumes(MediaType.APPLICATION_JSON)
	@Produces(MediaType.APPLICATION_JSON)
	//获得第一类产品信息
	public String getGoodsInfo(@PathParam("classify") String classify) { 
	    List<Image> infoList = shopService.findGoodsInfoByClassify(classify); 
	    Map map = new HashMap();
        map.put("goodsInfo", infoList);
		JSONObject jsonUser = JSONObject.fromObject(map);
		return jsonUser.toString();
	}
	
	@GET
	@Path("/getGoodsDetail/{imgurl}")
	@Consumes(MediaType.APPLICATION_JSON)
	@Produces(MediaType.APPLICATION_JSON)
	//点击图片后,获取产品详细信息
	public String getGoodsDetail(@PathParam("imgurl") String url){
		url = "../images/" + url;
		List<Image> imageList = shopService.findGoodsInfoByUrl(url);
		if(imageList == null){
			return "flase";
		}
		Image image = imageList.get(0);
		//查到图片信息后,根据id查询图片详细信息
		List<ImageDetail> detailList = shopService.findGoodsDetailByParentId(image.getId());
		if (detailList ==null) {
			return "notUploadByShopper";
		}
		Map map = new HashMap();
		map.put("imageInfo", imageList);
		map.put("imageDetail", detailList);
		JSONObject jsonUser = JSONObject.fromObject(map);
		return jsonUser.toString();
	}
	
	@GET
	@Path("/deleteShopCart/{id}")
	@Consumes(MediaType.APPLICATION_JSON)
	@Produces(MediaType.APPLICATION_JSON)
	public String deleteShopCart(@PathParam("id") Integer id){
		boolean flag =  shopService.deleteShopCart(id);
		if(flag){
			message = "success";
		}else{
			message = "false";
		}
		JSONObject jsonObject = new JSONObject();
		jsonObject.put("message", message);
		return jsonObject.toString();
	}
	public ShopService getShopService() {
		return shopService;
	}

	public void setShopService(ShopService shopService) {
		this.shopService = shopService;
	}

}
