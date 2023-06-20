package com.barcelonactiva.tech4good.hackathon.model.services;

import com.barcelonactiva.tech4good.hackathon.model.domain.ShopDocument;
import com.barcelonactiva.tech4good.hackathon.model.dto.ShopDTO;
import com.barcelonactiva.tech4good.hackathon.model.repository.IShopRepository;
import org.modelmapper.ModelMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.stream.Collectors;

@Service
public class ShopServiceImpl implements IShopService {

    @Autowired
    IShopRepository tiendaRepository;
    @Autowired
    private ModelMapper modelMapper;

    private ShopDTO convertShopToDTO(ShopDocument shop) {
        return modelMapper.map(shop, ShopDTO.class);
    }
    private List<ShopDTO> convertShopListToDTO(List<ShopDocument> shopsHistory) {
        return shopsHistory.stream().map(this::convertShopToDTO).collect(Collectors.toList());
    }

    @Override
    public List<ShopDTO> getActivitySectorById(String id) {
        List<ShopDocument> shops = tiendaRepository.findByActivitySectorCode(id);
        return convertShopListToDTO(shops);
    }

    @Override
    public List<ShopDTO> getActivityGroupById(String id) {
        List<ShopDocument> shops = tiendaRepository.findByActivityGroupCode(id);
        return convertShopListToDTO(shops);
    }

    @Override
    public List<ShopDTO> getNeighbourhoodCodeById(String id) {
        List<ShopDocument> shops = tiendaRepository.findByNeighbourhoodCode(id);
        return convertShopListToDTO(shops);
    }

    @Override
    public List<ShopDTO> getDistrictById(String id) {
        List<ShopDocument> shops = tiendaRepository.findByDistrictCode(id);
        return convertShopListToDTO(shops);
    }
}
