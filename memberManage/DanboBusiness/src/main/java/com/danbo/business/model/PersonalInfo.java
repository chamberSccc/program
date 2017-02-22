package com.danbo.business.model;

import javax.xml.bind.annotation.XmlRootElement;

@XmlRootElement(name="personalInfo")
public class PersonalInfo {
	private Integer id;
	private String  classify;
	private String  info;
	private String  detail;
	public Integer getId() {
		return id;
	}
	public void setId(Integer id) {
		this.id = id;
	}
	public String getClassify() {
		return classify;
	}
	public void setClassify(String classify) {
		this.classify = classify;
	}
	public String getInfo() {
		return info;
	}
	public void setInfo(String info) {
		this.info = info;
	}
	public String getDetail() {
		return detail;
	}
	public void setDetail(String detail) {
		this.detail = detail;
	}
	
}
