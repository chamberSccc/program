package com.danbo.business.dao;

import java.util.ArrayList;
import java.util.List;
import javax.annotation.Resource;

import org.glassfish.grizzly.nio.transport.UDPNIOAsyncQueueReader;
import org.springframework.orm.hibernate4.HibernateTemplate;
import org.springframework.stereotype.Repository;

import com.danbo.business.model.Param;
import com.danbo.business.model.PersonalInfo;
import com.danbo.business.model.User;

@Repository(value="userDao")
public class UserDao {

	@Resource(name="hibernateTemplate")
	private HibernateTemplate hibernateTemplate;
	
	//根据用户名和密码查询,用于登录,更改密码
	public List<User>  findByNameAndPassword (User user) {
	   String queryString = "from User where loginname = :loginname and password = :password";
	   String paramNames[] = {"loginname" , "password"};
	   String paramValues[] = {user.getLoginname(),user.getPassword()};
	   
	   @SuppressWarnings("unchecked")
	   List<User> listUsers = (List<User>) hibernateTemplate.findByNamedParam(queryString, paramNames, paramValues);
       return listUsers;		
	}
	//根据用户名和二级密码查询,用于更改二级密码
	public List<User>  findByNameAndPassword1 (User user) {
		   String queryString = "from User where loginname = :loginname and password1 = :password1";
		   String paramNames[] = {"loginname" , "password1"};
		   String paramValues[] = {user.getLoginname(),user.getPassword1()};
		   
		   @SuppressWarnings("unchecked")
		   List<User> listUsers = (List<User>) hibernateTemplate.findByNamedParam(queryString, paramNames, paramValues);
	       return listUsers;		
		}
	//根据身份证号查询,用于检查身份证号是否重复
	@SuppressWarnings("unchecked")
	public  List<User> checkUserIdNumber(String idnumber) {
		List<User> userList = new ArrayList<User>();
		String queryString = "from User where idnumber =:idnumber";
		userList = (List<User>) hibernateTemplate.findByNamedParam(queryString,"idnumber",idnumber);
        return userList;
	}	
	//根据会员编号查询,用于获得user实体类
	@SuppressWarnings("unchecked")
	public  List<User> findUserByLoginName(String loginname) {
			List<User> userList = new ArrayList<User>();
			String queryString = "from User where loginname =:loginname";
			userList = (List<User>) hibernateTemplate.findByNamedParam(queryString,"loginname",loginname);
	        return userList;
	}
	//根据分类,获得用户个人首页信息
	@SuppressWarnings("unchecked")
	public List<PersonalInfo> findPersonaInfoByClassify(String classify){
		List<PersonalInfo> infoList = new ArrayList<PersonalInfo>();
		String queryString = "from PersonalInfo where classify = :classify";
		infoList =(List<PersonalInfo>) hibernateTemplate.findByNamedParam(queryString,"classify",classify);
		return infoList;
	}
	//根据会员编号查询下级会员;
		@SuppressWarnings("unchecked")
	public  List<User> findNextUserByLoginName(String loginname) {
			List<User> userList = new ArrayList<User>();
			String queryString = "from User where recommendid =:loginname";
			userList = (List<User>) hibernateTemplate.findByNamedParam(queryString,"loginname",loginname);
	        return userList;
	}	
	//添加用户,注册
	public boolean  addUser(User user) {
	    try {
	    	hibernateTemplate.save(user);   
		} catch (Exception e) {
           return false;			
		}
	    return true;
	}
	// 查询用户编号参数
	public List<Param> findParam(String paramname){
		String queryString = "from Param where paramname =:paramname";
		List<Param> paramList = new ArrayList<Param>();
		paramList = (List<Param>) hibernateTemplate.findByNamedParam(queryString,"paramname",paramname);
		return paramList;		
	}
	//修改参数信息 
	public boolean updateParam(Param param){
		try {
			hibernateTemplate.update(param);
		} catch (Exception e) {
			return false;
		}
		return true;
	}
	//修改用户
	public boolean updateUser(User user){
		try {
			hibernateTemplate.update(user);
		} catch (Exception e) {
			return false;
		}
		return true;
	}
}
