package com.danbo.business.service;

import java.util.List;
import javax.annotation.Resource;
import org.springframework.stereotype.Service;
import com.danbo.business.dao.UserDao;
import com.danbo.business.model.Param;
import com.danbo.business.model.PersonalInfo;
import com.danbo.business.model.User;

@Service(value="userService")
public class UserService {

	@Resource(name="userDao")
	private UserDao userDao;
	//登录验证,更改一级密码
	public User findUserByNameAndPassword (User user) {
		List<User> listUsers = userDao.findByNameAndPassword(user);		
		if(listUsers.size() > 0) {
			return listUsers.get(0);
		}
		return null;
	}
	//用于更改更改二级密码
	public User findUserByNameAndPassword1 (User user) {
		List<User> listUsers = userDao.findByNameAndPassword1(user);		
		if(listUsers.size() > 0) {
			return listUsers.get(0);
		}
		return null;
	}
	//注册用户	
	public String addUser(User user) {
		String addUserReturn = "false";
		//注册之前,应该先检查注册数据在数据库中是否已经存在	
		List<User> redundIdNumber = userDao.checkUserIdNumber(user.getIdnumber());
		if(redundIdNumber.size()>0){
			addUserReturn = "redundIdNumber";
			return addUserReturn;
		}
		List<Param> paramLists = userDao.findParam("会员编号");
		Param param = new Param();
		String Thisloginname = ""; 
		if(paramLists.size()>0){
		    param = paramLists.get(0);
		    Thisloginname = param.getParamvalue();  
			user.setLoginname(Thisloginname);
		}else{
			addUserReturn = "errorParam";
			return addUserReturn;
		}
		boolean ifAdd = userDao.addUser(user);
		//如果注册成功,编号加1返回数据库
		if(ifAdd){
			Integer temp = Integer.parseInt(param.getParamvalue());
			temp = temp +1;			
			param.setParamvalue(temp.toString());
			userDao.updateParam(param);
			addUserReturn = "success" + Thisloginname;
		}
		return addUserReturn;
	}
	//根据会员编号获得User实体类
	public User findUserByLoginName(String loginname){
		List<User> listUsers = userDao.findUserByLoginName(loginname);
		if(listUsers.size() > 0) {
			return listUsers.get(0);
		}
		return null;
	}
	//根据会员编号获得所有下级会员
	public List<User> findNextUserByLoginName(String loginname){
		List<User> listUsers = userDao.findNextUserByLoginName(loginname);
		if(listUsers.size() > 0) {
			return listUsers;
		}
		return null;
	}
	public boolean updateUser(User user){
		return userDao.updateUser(user);
	}
	//根据分类,获得个人首页信息
	public List<PersonalInfo> findPersonaInfoByClassify(String classify){
		List<PersonalInfo> listInfo = userDao.findPersonaInfoByClassify(classify);
		if(listInfo.size() > 0){
			return listInfo;
		}
		return null;
	}
	public UserDao getUserDao() {
		return userDao;
	}
	public void setUserDao(UserDao userDao) {
		this.userDao = userDao;
	}
}
