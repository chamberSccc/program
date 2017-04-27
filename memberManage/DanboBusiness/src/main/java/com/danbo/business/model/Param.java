package com.danbo.business.model;

import javax.xml.bind.annotation.XmlRootElement;

@XmlRootElement(name="param")
public class Param {
	private Integer id;
	private String paramname;
	private String paramvalue;
	public Integer getId() {
		return id;
	}
	public void setId(Integer id) {
		this.id = id;
	}
	public String getParamname() {
		return paramname;
	}
	public void setParamname(String paramname) {
		this.paramname = paramname;
	}
	public String getParamvalue() {
		return paramvalue;
	}
	public void setParamvalue(String paramvalue) {
		this.paramvalue = paramvalue;
	}

}
