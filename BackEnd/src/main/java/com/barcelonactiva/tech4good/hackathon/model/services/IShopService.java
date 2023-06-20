package com.barcelonactiva.tech4good.hackathon.model.services;

import com.barcelonactiva.tech4good.hackathon.model.dto.ShopDTO;

import java.util.List;

public interface IShopService {

    List<ShopDTO> getActivitySectorById(String id);
    List<ShopDTO> getActivityGroupById(String id);
    List<ShopDTO> getNeighbourhoodCodeById(String id);
    List<ShopDTO> getDistrictById(String id);

}
