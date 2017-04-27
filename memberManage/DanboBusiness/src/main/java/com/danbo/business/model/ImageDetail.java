package com.danbo.business.model;

import javax.xml.bind.annotation.XmlRootElement;

@XmlRootElement(name="imageDetail")
public class ImageDetail {
	private Integer id;
	private String url;
	private Integer parentid;
	public Integer getId() {
		return id;
	}
	public void setId(Integer id) {
		this.id = id;
	}
	public String getUrl() {
		return url;
	}
	public void setUrl(String url) {
		this.url = url;
	}
	public Integer getParentid() {
		return parentid;
	}
	public void setParentid(Integer parentid) {
		this.parentid = parentid;
	}
	

}
