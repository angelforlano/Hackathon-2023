package com.barcelonactiva.tech4good.hackathon.model.domain;

import lombok.Getter;
import lombok.Setter;
import lombok.ToString;
import org.bson.types.ObjectId;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

import java.io.Serializable;

@Document
@Getter
@Setter
@ToString
public class ActivityDocument implements Serializable {

    private static final long serialVersionUID = 1L;

    @Id
    private ObjectId _id;
  
}
