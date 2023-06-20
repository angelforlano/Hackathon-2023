package com.barcelonactiva.tech4good.hackathon.model.domain.services;

import com.barcelonactiva.tech4good.hackathon.model.repository.ITiendaRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class TiendaServiceImpl implements ITiendaService{

    @Autowired
    ITiendaRepository tiendaRepository;
}
