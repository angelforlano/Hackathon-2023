package com.barcelonactiva.tech4good.hackathon.model.domain;

import lombok.Getter;
import lombok.Setter;
import lombok.ToString;
import org.bson.types.ObjectId;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;
import org.springframework.data.mongodb.core.mapping.Field;

import java.io.Serializable;

@Document(collection = "shops")
@Getter
@Setter
@ToString
public class ActivityDocument implements Serializable {

    private static final long serialVersionUID = 1L;

    @Id
    private ObjectId _id;
    @Field(name = "Codi_Principal_Activitat")
    private String activityMainCode;
    @Field(name = "Nom_Principal_Activitat")
    private String activityMainName;
    @Field(name = "Codi_Sector_Activitat") 
    private String activitySectorCode;
    @Field(name = "Nom_Sector_Activitat")
    private String activitySectorName;
    @Field(name = "Codi_Grup_Activitat")
    private String activityGroupCode;
    @Field(name = "Nom_Grup_Activitat")
    private String activityGroupName;
    @Field(name = "Nom_Local")
    private String localName;
    @Field(name = "SN_Oci_Nocturn")
    private boolean nightlife;
    @Field(name = "SN_Obert24h")
    private boolean open24h;
    @Field(name = "SN_Carrer")
    private boolean street;
    @Field(name = "Nom_Mercat")
    private String marketName;
    @Field(name = "Nom_Galeria")
    private String galleryName;
    @Field(name = "Nom_CComercial")
    private String shoppingCenterName;
    @Field(name = "Direccio_Unica")
    private String uniqueAddress;
    @Field(name = "Codi_Via")
    private String streetCode;
    @Field(name = "Nom_Via")
    private String streetName;
    @Field(name = "Codi_Barri")
    private String neighbourhoodCode;
    @Field(name = "Nom_Barri")
    private String neighbourhoodName;
    @Field(name = "Codi_Districte")
    private String districtCode;
    @Field(name = "Nom_Districte")
    private String districtName;






}
