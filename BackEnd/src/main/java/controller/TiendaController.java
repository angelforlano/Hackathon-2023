package controller;

import com.barcelonactiva.tech4good.hackathon.model.services.ActivityServiceImpl;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class TiendaController {

    @Autowired
    ActivityServiceImpl tiendaServiceImpl;
    @GetMapping("/sector/{id}")
    public ResponseEntity<?> obtenerActivitySectorCode(@PathVariable String id){
        ResponseEntity<?> responseEntity = null;
        return responseEntity;
    }

    @GetMapping("/grupo/{id}")
    public ResponseEntity<?> obtenerActivityGroupCode(@PathVariable String id){
        ResponseEntity<?> responseEntity = null;
        return responseEntity;
    }

    @GetMapping("/ubicacion/codigoPostal/{id}")
    public ResponseEntity<?> obtenerStreetCode(@PathVariable String id){
        ResponseEntity<?> responseEntity = null;
        return responseEntity;
    }

    @GetMapping("/ubicacion/barrio/{id}")
    public ResponseEntity<?> obtenerNeighbourhoodCode(@PathVariable String id){
        ResponseEntity<?> responseEntity = null;
        return responseEntity;
    }

    @GetMapping("/ubicacion/distrito/{id}")
    public ResponseEntity<?> obtenerDistrictCode(@PathVariable String id){
        ResponseEntity<?> responseEntity = null;
        return responseEntity;
    }
}
