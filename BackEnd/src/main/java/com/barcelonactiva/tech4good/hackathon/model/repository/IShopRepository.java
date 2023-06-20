package com.barcelonactiva.tech4good.hackathon.model.repository;

import com.barcelonactiva.tech4good.hackathon.model.domain.ShopDocument;
import org.bson.types.ObjectId;
import org.springframework.data.mongodb.repository.MongoRepository;

import java.util.List;

public interface IShopRepository extends MongoRepository<ShopDocument, ObjectId> {

    List<ShopDocument> findBySectorId(String id);
    List<ShopDocument> findByGroupId(String id);
    List<ShopDocument> findByStreetId(String id);
    List<ShopDocument> findByNeighbourhoodId(String id);
    List<ShopDocument> findByDistrictId(String id);


}
