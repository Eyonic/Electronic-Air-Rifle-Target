<?php

use Illuminate\Support\Facades\Route;
use App\Models\Shot;
use Illuminate\Http\JsonResponse;
use Illuminate\Support\Facades\DB;

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider and all of them will
| be assigned to the "web" middleware group. Make something great!
|
*/

/*
|--------------------------------------------------------------------------
| Shooting Club web.php 
|--------------------------------------------------------------------------
*/





Route::get('/target', function () {

  return view('target-v1');
});



/*
|--------------------------------------------------------------------------
| Api
|--------------------------------------------------------------------------
*/


Route::get('/electronic-air-rifle-target', function () {

 $shots = Shot::all();

  $json = [
        "target" => $shots->map(function ($shot) {
            return [
                "shot" => $shot->shot,
                "x" => $shot->x,
                "z" => $shot->z,
            ];
        })->toArray(),
    ];



  return response()->json($json)
       ->header('Access-Control-Allow-Origin', '*')
       ->header('Access-Control-Allow-Methods', 'GET');


});



/*
|--------------------------------------------------------------------------
| Bullets-API_Information
|--------------------------------------------------------------------------
*/



Route::get('/add-shot/shot/{schot}/x/{x}/z/{z}', function ($shot, $x, $z) {
    // Save the shot to the database using the DB facade
    DB::table('shots')->insert([
        'shot' => $shot,
        'x' => $x,
        'z' => $z,
    ]);
    // Don't redirect this one, Course it could messup the arduino code
    return "Shot added successfully!";
});



Route::get('/delete-shot', function () {
  // Delete all shots from the database
  \App\Models\Shot::truncate();

  // Redirect to /target after deletion
  return redirect('/target')->with('success', 'All shots deleted successfully!');
});
