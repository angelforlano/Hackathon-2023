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

    private String localName;
    private String activitySectorCode;
    private String activityGroupCode;
    private String streetCode;
    private String neighbourhoodCode;
}
