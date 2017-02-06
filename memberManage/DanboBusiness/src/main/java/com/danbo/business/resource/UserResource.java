package com.danbo.business.resource;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

import javax.annotation.Resource;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpSession;
import javax.ws.rs.Consumes;
import javax.ws.rs.DELETE;
import javax.ws.rs.GET;
import javax.ws.rs.POST;
import javax.ws.rs.PUT;
import javax.ws.rs.Path;
import javax.ws.rs.PathParam;
import javax.ws.rs.Produces;
import javax.ws.rs.core.Context;
import javax.ws.rs.core.MediaType;
import net.sf.json.JSONObject;
import org.springframework.context.annotation.Scope;
import org.springframework.stereotype.Component;

import com.danbo.business.model.PersonalInfo;
import com.danbo.business.model.User;
import com.danbo.business.service.UserService;
import com.sun.research.ws.wadl.Request;

/**
 * Spring 使用Component注解Jersey资源类
 * Path：相当于Spring MVC中的RequestMapping，用于HTTP URL请求
 * Scope：表示Spring的单例模式或者原型模式prototype
 */
@Component
@Path("/user")
@Scope("prototype")
public class UserResource {

	@Resource(name = "userService")
	private UserService userService;
	private String message;

	/**
	 * GET：表示Jersey rest查询请求
	 * Path:此处完整路径需接类上面的Path,如：user/exist/xx/1233，才会跳转到该方法处理
	 * Consumes:表示前端请求数据格式
	 * Produces:表示返回值数据格式
	 * PathParam:用于注解参数变量，与URL中对应的变量名对应，达到传递的作用
	 */
	@GET
	@Path("/exist/{loginname}/{password}")
	@Consumes(MediaType.APPLICATION_JSON)
	@Produces(MediaType.APPLICATION_JSON)
	//登录验证
	public String isExist(@PathParam("loginname") String loginname,
			@PathParam("password") String password,
			@Context HttpServletRequest request) {
		User user = new User();
		user.setLoginname(loginname);
		user.setPassword(password);
		User result = userService.findUserByNameAndPassword(user);
		if(result != null)
		{
			request.getSession().setAttribute("loginname", loginname);
		}
		
		/**
		 * Spring+Jersey框架，不会主动帮助我们将传递的对象转换成JSON数据格式，
		 * 需使用JSON lib类中的JSONObject或者JSONArray转换才能够传递，否则前端
		 * 会报302错误。
		 */
		JSONObject jsonUser = JSONObject.fromObject(result);
		return jsonUser.toString();
	}
	
	@GET
	@Path("/validate")
	@Consumes(MediaType.APPLICATION_JSON)
	@Produces(MediaType.APPLICATION_JSON)
	//管理员登录验证
	public String validate(@Context HttpServletRequest request) {
		String loginname = "";
		HttpSession session = request.getSession(false); 
	    if(session != null){
	    	Object sessionObj =  session.getAttribute("loginname");   
	    	loginname = (String) sessionObj; 
	    	if(loginname.equals("admin")){
		    	message = "success";
		    }else{
		    	message = "error";
		    }
	    }
	    else{
	    	message = "notLogin";
	    }
	    JSONObject jsonObject = new JSONObject();
		jsonObject.put("message", message);
		return jsonObject.toString();
	}
	
	@GET
	@Path("/getUserInfo")
	@Consumes(MediaType.APPLICATION_JSON)
	@Produces(MediaType.APPLICATION_JSON)
	//获取用户信息
	public String getUserInfo(@Context HttpServletRequest request) {
		String loginname = "";
		HttpSession session = request.getSession(false); 
	    if(session != null){
	    	Object sessionObj =  session.getAttribute("loginname"); 
	    	loginname = (String) sessionObj; 
	    	User user = new User();
		    user = userService.findUserByLoginName(loginname);
		    if(user!=null){
		    	JSONObject jsonUser = JSONObject.fromObject(user);
		    	message = jsonUser.toString();
		    }	    	
	    }else{
	    	message = "error";
	    }
	    JSONObject jsonObject = new JSONObject();
		jsonObject.put("message", message);
		return jsonObject.toString();
	}
	
	@GET
	@Path("/getPersonalInfo")
	@Consumes(MediaType.APPLICATION_JSON)
	@Produces(MediaType.APPLICATION_JSON)
	//获得个人首页信息
	public String getPersonalInfo() { 
		//奖金信息
	    List<PersonalInfo> infoList = userService.findPersonaInfoByClassify("奖金");
	    List<PersonalInfo> messageList = userService.findPersonaInfoByClassify("留言"); 
	    if(infoList == null || messageList == null){
	    	return null;
	    }
	    Map map = new HashMap();
        map.put("personal", infoList);
        map.put("message", messageList);
		JSONObject jsonUser = JSONObject.fromObject(map);
		return jsonUser.toString();
	}

	@GET
	@Path("/getDirMember")
	@Consumes(MediaType.APPLICATION_JSON)
	@Produces(MediaType.APPLICATION_JSON)
	//查询直属会员列表
	public String getDirMember(@Context HttpServletRequest request) {
		String loginname = "";
		HttpSession session = request.getSession(false); 
	    if(session != null){  
	    	Object sessionObj =  session.getAttribute("loginname");   
	    	loginname = (String) sessionObj;
	      } 
	    List<User> userList = userService.findNextUserByLoginName(loginname); 
	    Map map = new HashMap();
        map.put("aaData", userList);
		JSONObject jsonUser = JSONObject.fromObject(map);
		return jsonUser.toString();
	}
	
	@POST
	@Path("/addUser")
	@Consumes(MediaType.APPLICATION_JSON)
	@Produces(MediaType.APPLICATION_JSON)
	//添加
	public String addUser(User user) {
		String message = userService.addUser(user);
		JSONObject jsonObject = new JSONObject();
		jsonObject.put("message", message);
		return jsonObject.toString();
	}
	@PUT
	@Path("/updateUser")
	@Consumes(MediaType.APPLICATION_JSON)
	@Produces(MediaType.APPLICATION_JSON)
	//修改密码提示问题
	public String updateUser(User htmluser,@Context HttpServletRequest request) {
		String loginname = "";
		HttpSession session = request.getSession(false); 
	    if(session != null){  
	    	Object sessionObj =  session.getAttribute("loginname");   
	    	loginname = (String) sessionObj;
	      } 
	    User user = new User();
	    user = userService.findUserByLoginName(loginname);
	    if(user !=null){
	    	user.setQuestion1(htmluser.getQuestion1());
	    	user.setQuestion2(htmluser.getQuestion2());
	    	user.setQuestion3(htmluser.getQuestion3());
	    	user.setAnswer1(htmluser.getAnswer1());
	    	user.setAnswer2(htmluser.getAnswer2());
	    	user.setAnswer3(htmluser.getAnswer3());
	    }
		boolean flag = userService.updateUser(user);
		if (flag) {
			message = "success";
		} else {
			message = "fail";
		}
		JSONObject jsonObject = new JSONObject();
		jsonObject.put("message", message);
		return jsonObject.toString();
	}
	
	@PUT
	@Path("/updatePassword/{password}/{newpassword}")
	@Consumes(MediaType.APPLICATION_JSON)
	@Produces(MediaType.APPLICATION_JSON)
	//修改一级密码
	public String updatePassWord(@PathParam("password") String password,
			@PathParam("newpassword") String newpassword,
			@Context HttpServletRequest request) {
		String loginname = "";
		HttpSession session = request.getSession(false); 
	    if(session != null){  
	    	Object sessionObj =  session.getAttribute("loginname");   
	    	loginname = (String) sessionObj;
	      } 
	    User user = new User();
	    user.setLoginname(loginname);
	    user.setPassword(password);
	    User user1 = new User();	    
	    user1 = userService.findUserByNameAndPassword(user);
	    JSONObject jsonObject = new JSONObject();
	    //如果账号密码正确
	    if(user1 !=null){
	    	user1.setPassword(newpassword);
	    }else{
	    	message = "errorPassword";
			jsonObject.put("message", message);
			return jsonObject.toString();
	    }
		boolean flag = userService.updateUser(user1);
		if (flag) {
			message = "success";
		} else {
			message = "fail";
		}		
		jsonObject.put("message", message);
		return jsonObject.toString();
	}
	@PUT
	@Path("/updatePassword1/{password1}/{newpassword1}")
	@Consumes(MediaType.APPLICATION_JSON)
	@Produces(MediaType.APPLICATION_JSON)
	//修改一级密码
	public String updatePassWord1(@PathParam("password1") String password1,
			@PathParam("newpassword1") String newpassword1,
			@Context HttpServletRequest request) {
		String loginname = "";
		HttpSession session = request.getSession(false); 
	    if(session != null){  
	    	Object sessionObj =  session.getAttribute("loginname");   
	    	loginname = (String) sessionObj;
	      } 
	    User user = new User();
	    user.setLoginname(loginname);
	    user.setPassword1(password1);
	    User user1 = new User();	    
	    user1 = userService.findUserByNameAndPassword1(user);
	    JSONObject jsonObject = new JSONObject();
	    //如果账号密码正确
	    if(user1 !=null){
	    	user1.setPassword1(newpassword1);;
	    }else{
	    	message = "errorPassword1";
			jsonObject.put("message", message);
			return jsonObject.toString();
	    }
		boolean flag = userService.updateUser(user1);
		if (flag) {
			message = "success";
		} else {
			message = "fail";
		}		
		jsonObject.put("message", message);
		return jsonObject.toString();
	}
	public void setUserService(UserService userService) {
		this.userService = userService;
	}
}
