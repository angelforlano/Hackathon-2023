package controller;

import com.barcelonactiva.tech4good.hackathon.model.domain.services.TiendaServiceImpl;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class TiendaController {

    @Autowired
    TiendaServiceImpl tiendaServiceImpl;
}
