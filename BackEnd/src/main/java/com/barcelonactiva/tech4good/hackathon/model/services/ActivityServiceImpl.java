package com.barcelonactiva.tech4good.hackathon.model.services;

import com.barcelonactiva.tech4good.hackathon.model.repository.IActivityRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class ActivityServiceImpl implements IActivityService {

    @Autowired
    IActivityRepository tiendaRepository;
}
