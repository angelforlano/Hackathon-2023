package com.barcelonactiva.tech4good.hackathon.model.repository;

import com.barcelonactiva.tech4good.hackathon.model.domain.ShopDocument;
import org.bson.types.ObjectId;
import org.springframework.data.mongodb.repository.MongoRepository;

public interface IShopRepository extends MongoRepository<ShopDocument, ObjectId> {
}
