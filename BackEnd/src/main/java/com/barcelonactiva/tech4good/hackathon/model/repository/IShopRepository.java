package com.barcelonactiva.tech4good.hackathon.model.repository;

import com.barcelonactiva.tech4good.hackathon.model.domain.ShopDocument;
import org.bson.types.ObjectId;
import org.springframework.data.mongodb.repository.MongoRepository;

import java.util.List;

public interface IShopRepository extends MongoRepository<ShopDocument, ObjectId> {


    List<ShopDocument> findByActivitySectorCode(String id);
    List<ShopDocument> findByActivityGroupCode(String id);
    List<ShopDocument> findByStreetCode(String id);
    List<ShopDocument> findByNeighbourhoodCode(String id);
    List<ShopDocument> findByDistrictCode(String id);


}

