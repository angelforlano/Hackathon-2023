package com.barcelonactiva.tech4good.hackathon.model.services;

import com.barcelonactiva.tech4good.hackathon.model.repository.IShopRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class ShopServiceImpl implements IShopService {

    @Autowired
    IShopRepository tiendaRepository;
}
