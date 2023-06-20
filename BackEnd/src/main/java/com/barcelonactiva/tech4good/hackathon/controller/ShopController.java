package com.barcelonactiva.tech4good.hackathon.controller;

import com.barcelonactiva.tech4good.hackathon.model.dto.ShopDTO;
import com.barcelonactiva.tech4good.hackathon.model.services.ShopServiceImpl;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
public class ShopController {

    @Autowired
    ShopServiceImpl shopServiceImpl;
    @GetMapping("/sector/{id}")
    public ResponseEntity<?> obtenerActivitySectorCode(@PathVariable String id){
        ResponseEntity<?> responseEntity;
        List<ShopDTO> listSectorId = shopServiceImpl.getActivitySectorById(id);
        responseEntity = ResponseEntity.status(HttpStatus.OK).body(listSectorId);
        return responseEntity;
    }

    @GetMapping("/grupo/{id}")
    public ResponseEntity<?> obtenerActivityGroupCode(@PathVariable String id){
        ResponseEntity<?> responseEntity;
        List<ShopDTO> listGroupId = shopServiceImpl.getActivityGroupById(id);
        responseEntity = ResponseEntity.status(HttpStatus.OK).body(listGroupId);
        return responseEntity;
    }

    @GetMapping("/ubicacion/codigoPostal/{id}")
    public ResponseEntity<?> obtenerStreetCode(@PathVariable String id){
        ResponseEntity<?> responseEntity;
        List<ShopDTO> listStreetCodeId = shopServiceImpl.getStreetCodeById(id);
        responseEntity = ResponseEntity.status(HttpStatus.OK).body(listStreetCodeId);
        return responseEntity;
    }

    @GetMapping("/ubicacion/barrio/{id}")
    public ResponseEntity<?> obtenerNeighbourhoodCode(@PathVariable String id){
        ResponseEntity<?> responseEntity = null;
        List<ShopDTO> listNeighbourhoodCodeId = shopServiceImpl.getNeighbourhoodCodeById(id);
        responseEntity = ResponseEntity.status(HttpStatus.OK).body(listNeighbourhoodCodeId);
        return responseEntity;
    }

    @GetMapping("/ubicacion/distrito/{id}")
    public ResponseEntity<?> obtenerDistrictCode(@PathVariable String id){
        ResponseEntity<?> responseEntity = null;
        List<ShopDTO> listDistrictId = shopServiceImpl.getDistrictById(id);
        responseEntity = ResponseEntity.status(HttpStatus.OK).body(listDistrictId);
        return responseEntity;
    }
}