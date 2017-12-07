<?php
defined('BASEPATH') OR exit('No direct script access allowed');

class Service extends CI_Controller 
{
	public function __construct()
	{
		parent::__construct();
		error_reporting(0);
		$this->load->model("service_model");
		$this->load->helper('my');
	}
	public function getSuggestions()
	{
		$param = array("key" => addslashes(urldecode($_GET['key'])));
		$query = $this->service_model->get_suggestions($param);
		if($query->num_rows() > 0)
		{
			foreach($query->result() as $row)
			{
				$results[] = array("title" => $row->title, "poster" => $row->thumbnail_url);
			}
			$responce = array("success" => true, "results" => $results, "total" => $query->num_rows());
			echo json_encode($responce);die();
		}
	}
	public function getSearchResults()
	{
		if(!$this->input->post())
		{
			die("401 Forbidden");
		}
		$param = array(
							"search_key" => addslashes($this->input->post('search_key')),
							"offset"	 => $this->input->post('offset')
						);
		$total_records = $this->service_model->result_count($param);
		$param['limit'] = LIMIT;
		$query = $this->service_model->get_results($param);
		//echo $this->db->last_query();
		if($total_records>0)
		{
			$movie_ids = array();
			foreach($query->result() as $row)
			{
				$movie_auto_id 			= $row->movie_auto_id;
				array_push($movie_ids, $movie_auto_id);
				$movie_title 			= $row->movie_title;
				$movie_release_year 	= $row->movie_release_year;
				$movie_thumbnail_url 	= $row->movie_thumbnail_url;
				$price_auto_ids 			= explode(',|,', $row->price_auto_id);
				$a = 0;
				foreach($price_auto_ids as $price_id)
				{
					$vendor_ids 			= explode(',|,', $row->vendor_id);
					$vendor_id   			= $vendor_ids[$a];
					$vender_names 			= explode(',|,', $row->vender_name);
					$vender_name 			= $vender_names[$a];
					$vender_thumbnail_urls 	= explode(',|,', $row->vender_thumbnail_url);
					$vender_thumbnail_url	= $vender_thumbnail_urls[$a];
					$movie_video_urls 		= explode(',|,', $row->movie_video_url);
					$movie_video_url 		= $movie_video_urls[$a];
					$movie_unique_ids 		= explode(',|,', $row->movie_unique_id);
					$movie_unique_id 		= $movie_unique_ids[$a];
					$price_Buy_sd_prices 	= explode(',|,', $row->price_Buy_sd_price);
					$price_Buy_sd_price 	= $price_Buy_sd_prices[$a];
					$price_Buy_hd_prices 	= explode(',|,', $row->price_Buy_hd_price);
					$price_Buy_hd_price 	= $price_Buy_hd_prices[$a];
					$price_Rent_sd_prices 	= explode(',|,', $row->price_Rent_sd_price);
					$price_Rent_sd_price 	= $price_Rent_sd_prices[$a];
					$price_Rent_hd_prices 	= explode(',|,', $row->price_Rent_hd_price);
					$price_Rent_hd_price 	= $price_Rent_hd_prices[$a];
					$is_subscribes			= explode(',|,', $row->is_subscribe);
					$is_subscribe 			= $is_subscribes[$a];
					$venders[$movie_auto_id][$vendor_id] = array(
																		"vender_name" 			=> $vender_name,
																		"vender_thumbnail_url"	=> $vender_thumbnail_url,
																		"vender_id"				=> $vendor_id,
																		"vender_url"			=> $movie_video_url,
																		"Buy_sd_price"			=> $price_Buy_sd_price, 
																		"Buy_hd_price"			=> $price_Buy_hd_price,
																		"Rent_sd_price"			=> $price_Rent_sd_price,
																		"Rent_hd_price"			=> $price_Rent_hd_price,
																		"is_subscribe"			=> $is_subscribe
																	);
					$a++;
				}
				$result[$movie_auto_id] = array(
												"auto_id"				=> $movie_auto_id,
												"show"					=> ($price_Buy_sd_price>0 || $price_Rent_sd_price>0 || $is_subscribe==1)?'sd_'.$movie_auto_id:'hd_'.$movie_auto_id,
												"movie_title"			=> $movie_title,
												"movie_thumbnail_url"	=> $movie_thumbnail_url,
												"release_year"			=> date('Y', strtotime($movie_release_year)),
												"venders"				=> $venders[$movie_auto_id],
											);
			}
			$update_array = array(
										"table"			=> "tbl_movies",
										"data"			=> array("`displayed_count`" => "`displayed_count`+1"),
										"where_in_field"=> "auto_id",
										"where_in"		=> $movie_ids
									);
			$this->Common_model->update_count($update_array);
			$responce = array("success" => true, "results" => $result, "total_records" => $total_records);
		}
		else
		{
			$responce = array("success" => false, "error" => "No Records found");
		}
		echoJson($responce);
	}
	public function clickCount()
	{
		$update_array = array(
									"table"			=> "tbl_movies",
									"data"			=> array("clicks_count" => "clicks_count+1"),
									"where"			=> array("auto_id" => $this->input->post('auto_id'))
								);
		$this->Common_model->update_count($update_array);
	}
	public function query()
	{
		echo '<form action="" method="post"><input style="width:96%;" type="text" value="'.$this->input->post('query').'" name="query"><input type="submit" value="Submit"></form>';
		if($this->input->post())
		{
			$query = "SELECT t1.auto_id AS movie_auto_id, 
							t1.title AS movie_title, 
							t1.thumbnail_url AS movie_thumbnail_url, 
							t2.thumbnail_url AS vender_thumbnail_url, 
							t3.video_url AS movie_video_url  
							FROM ".TBL_MOVIES." t1 
							LEFT JOIN tbl_prices t3 ON t1.auto_id=t3.movie_id
							LEFT JOIN tbl_vendors t2 ON t3.vendor_id=t2.auto_id WHERE t3.vendor_id=4";
			$result = $this->db->query($this->input->post('query')?$this->input->post('query'):$query);
			print_r($result->result());
		}


	}
}
