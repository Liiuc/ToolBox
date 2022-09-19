/* Function for calculate the distance from two points coordinates */
    function distanceAction($lat1, $lon1, $lat2, $lon2, $unit) {
        if (($lat1 == $lat2) && ($lon1 == $lon2)) {
          return 0;
        }else{
            $theta = $lon1 - $lon2;
            $dist = sin(deg2rad($lat1)) * sin(deg2rad($lat2)) +  cos(deg2rad($lat1)) * cos(deg2rad($lat2)) * cos(deg2rad($theta));
            $dist = acos($dist);
            $dist = rad2deg($dist);
            $miles = $dist * 60 * 1.1515;
            $unit = strtoupper($unit);
            if($unit == "K") {
                return ($miles * 1.609344);
            }else if ($unit == "N") {
                return ($miles * 0.8684);
            }else {
                return $miles;
            }
        }
    }
    
    /* Function for calculate the bearing between two points coordinates */
    function bearingAction($lat1, $lon1, $lat2, $lon2) {
         $teta1 = deg2rad($lat1);
         $teta2 = deg2rad($lat2);
         $delta1 = deg2rad($lat2-$lat2);
         $delta2 = deg2rad($lon2-$lon1);  
         
         $y=0.0;
         $x=0.0;
         $brng=0.0;
         
         $y= sin($delta2)* cos($teta2);
         $x= cos($teta1)*sin($teta2)-sin($teta1)*cos($teta2)*cos($delta2);
         $brng= atan2($y, $x);
         
         $brng= rad2deg($brng);
         $brng= (((int)$brng +360)%360);
         
         return $brng;
    }