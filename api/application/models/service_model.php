<?php 
class Service_model extends CI_Model
{
	public function __construct()
	{
		parent::__construct();
		define('TBL_MOVIES', 'tbl_movies');
	}
	public function get_suggestions($param)
	{
		$query = $this->db->query("SELECT title, thumbnail_url, SUM(displayed_count+clicks_count) AS clicks FROM ".TBL_MOVIES." WHERE REPLACE(LOWER(title),'-','') LIKE LOWER('".$param['key']."%') GROUP BY title ORDER BY clicks DESC, title ASC LIMIT 10");
		return $query;
	}
	public function get_results($param)
	{
		if($param['limit'])
			$append = " LIMIT ".$param['offset'].",".$param['limit'];
		$query = $this->db->query("SELECT t1.auto_id AS movie_auto_id, IF(REPLACE(LOWER(t1.title),'-','')=LOWER('".$param['search_key']."'), 1, 0) AS exact,
							t1.title AS movie_title, 
							t1.thumbnail_url AS movie_thumbnail_url, 
							t1.release_year AS movie_release_year, 
							GROUP_CONCAT(t2.auto_id SEPARATOR ',|,') AS vendor_id, 
							GROUP_CONCAT(t2.name SEPARATOR ',|,') AS vender_name, 
							GROUP_CONCAT(t2.thumbnail_url SEPARATOR ',|,') AS vender_thumbnail_url, 
							GROUP_CONCAT(t3.video_url SEPARATOR ',|,') AS movie_video_url, 
							GROUP_CONCAT(t3.unique_id SEPARATOR ',|,') AS movie_unique_id, 
							GROUP_CONCAT(t3.auto_id SEPARATOR ',|,') AS price_auto_id, 
							GROUP_CONCAT(t3.Buy_sd_price SEPARATOR ',|,') AS price_Buy_sd_price, 
							GROUP_CONCAT(t3.Buy_hd_price SEPARATOR ',|,') As price_Buy_hd_price, 
							GROUP_CONCAT(t3.Rent_sd_price SEPARATOR ',|,') AS price_Rent_sd_price, 
							GROUP_CONCAT(t3.Rent_hd_price SEPARATOR ',|,') AS price_Rent_hd_price,   
							GROUP_CONCAT(t3.is_subscribe SEPARATOR ',|,') AS is_subscribe   
							FROM ".TBL_MOVIES." t1 
							LEFT JOIN tbl_prices t3 ON t1.auto_id=t3.movie_id
							LEFT JOIN tbl_vendors t2 ON t3.vendor_id=t2.auto_id  
							WHERE (REPLACE(LOWER(t1.title),'-','') LIKE LOWER('%".$param['search_key']."%')) AND ((t3.Buy_sd_price>0 OR t3.Buy_hd_price>0 OR t3.Rent_sd_price>0 OR t3.Rent_hd_price>0) OR (t3.is_subscribe=1)) GROUP BY t3.movie_id ORDER BY exact DESC, t1.title, t1.release_year DESC, t3.Buy_sd_price,t3.Rent_sd_price, t3.Buy_hd_price, t3.Rent_hd_price ASC 
							".$append);
		return $query;
	}
	public function result_count($param)
	{
		$query = $this->db->query("SELECT t1.auto_id 
							FROM ".TBL_MOVIES." t1 
							LEFT JOIN tbl_prices t3 ON 
							t1.auto_id=t3.movie_id  
							LEFT JOIN tbl_vendors t2 ON 
							t3.vendor_id=t2.auto_id  
							WHERE (REPLACE(LOWER(title),'-','') LIKE LOWER('%".$param['search_key']."%')) AND ((t3.Buy_sd_price>0 OR t3.Buy_hd_price>0 OR t3.Rent_sd_price>0 OR t3.Rent_hd_price>0) OR (t3.is_subscribe=1)) GROUP BY t3.movie_id
							");
		return $query->num_rows();
	}
}
?>