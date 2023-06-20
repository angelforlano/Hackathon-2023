package com.barcelonactiva.tech4good.hackathon.model.dto;

import lombok.Getter;
import lombok.Setter;
import lombok.ToString;

import java.io.Serializable;

@Getter
@Setter
@ToString
public class ShopDTO implements Serializable {

    private static final long serialVersionUID = 1L;

    private String activitySectorName;
    private String activityGroupName;
    private String localName;
    private String neighbourhoodName;
    private String districtName;


}
