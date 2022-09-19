            /*Algo for salt consumption*/
         
            var segmento = [];                                                  //array temp per creare i segmenti
            var segmenti = [];                                                  //array di array con i segmenti
            var startSpread = 0;                                                //variabile usata come flag per capire se si e' gia' iniziato a spargere
            var dosage = [];
            var width = [];
            var distance = 0;                                                   //da calcolare
            var distSeg = [];
            var temp2 = 0;                                                      //variabile temporanea utilzzata per calcolare la distanza
            var tempLat = [];                                                   //tutti i lat
            var tempLong = [];                                                  //tutti i Long    
            var flag1 = 0;                                                      //flag che utilizzo per calcolare il dosaggio (essendoci due OP in ogni segmento)
            var totSalt = 0;
            var saltTemp = 0;
            var humidTemp = 0;
            var totHumid = 0; 
            var humid = [];
            
            /*Crea un array di array di segmenti dove si sparge*/
            $.each(wps, function(index, val){
                if('options' in val && 'operation_param' in val.options){       //controllo se il punto e' un OP(OP= PUNTO OPERAZIONALE)
                    if(Array.isArray(segmento) && segmento.length){             //controlla se segmentO  NON e' nullo, in caso sia nullo procede ,altrimenti va oltre
                        segmento.push(wps[index]);                              //metto il punto dentro segmento
                        segmenti.push(segmento);                                //metto segmento dentro segmenti
                        startSpread = 0;                                        //ogni volta che viene pushato un segment, azzero il flag  
                        segmento = [];                                          //pulisco il segmento     
                    }                  
                    if(val.latLng.on_duty){                                     //controllo se OP è on_duty=1 
                        segmento.push(wps[index]);                              //metto il punto all'interno del segmento
                        startSpread = 1;                                        //variabile impostata a 1 per permettere di inserire i punti del percorso senza OP ma dove si sparge.
                    }                                                     
                }else if(startSpread === 1){                                    //in caso il punto non sia un OP ma viene sparso in quel punto
                    segmento.push(wps[index]);                                  //inserisco il punto nel SEGMENTO
                }              
            });
            
            /*Crea un array di array di segmenti dove si sparge*/
            $.each(segmenti, function(i, val){                                                      //Foreach su SEGMENTI            
                flag1 = 0;
                $.each(val, function(j, elem){                                                      //Foreach SU SEGMENTO
                    if('options' in elem && 'operation_param' in elem.options && flag1 == 0){       //controllo che sia un OP CON DATI DI SPARGIMENTO
                        dosage[i] = elem.options.operation_param.dosage;
                        width[i] = elem.options.operation_param.width;
                        if($.trim(elem.options.operation_param.humidifier) == 'true'){
                            humid[i] = elem.options.operation_param.humidify;
                        }else{
                            humid[i] = 0;
                        }
                        flag1 = 1;
                    }   
                    tempLat[j] = elem.latLng.lat;                               //tutti i lat di un segmento
                    tempLong[j] = elem.latLng.lng;                              //tutti i Long di un segmento                      
                });
                $.each(val, function(j, elem){
                    if (tempLat[j+1] == null){ 
                        temp2 = 0;
                        distance = 0;
                        return false;
                    }else{
                        temp2 = getDistanceFromLatLonInM(tempLat[j], tempLong[j], tempLat[j+1], tempLong[j+1]);
                        distance = distance + temp2;
                        distSeg[i] = distance;
                    }
                });
                saltTemp = dosage[i] * width[i] * distSeg[i];
                humidTemp = distSeg[i] * humid[i];
                totHumid = totHumid + humidTemp;
                totSalt = totSalt + saltTemp;
                tempLat = [];                   //azzero
                tempLong = [];                  //azzero
            });
            totHumid = totHumid / 1000;
            totSalt = totSalt / 1000;

            $("#salt").html(Math.round(totSalt*100)/100 + "Kg");
            $("#humidifier").html(Math.round(totHumid*100)/100 + "Kg");

            function getDistanceFromLatLonInM(lat1,lon1,lat2,lon2) {
                var R = 6371; // Radius of the earth in km
                var dLat = deg2rad(lat2 - lat1);  // deg2rad below
                var dLon = deg2rad(lon2 - lon1); 
                var a = 
                    Math.sin(dLat / 2) * Math.sin(dLat / 2) +
                    Math.cos(deg2rad(lat1)) * Math.cos(deg2rad(lat2)) * 
                    Math.sin(dLon / 2) * Math.sin(dLon / 2)
                    ; 
                var c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1-a)); 
                // var d = R * c; // Distance in km
                var d = R * c * 1000; // DISTANZA IN METRI
                return d;
            }
            function deg2rad(deg) {
                return deg * (Math.PI / 180);
            }
            