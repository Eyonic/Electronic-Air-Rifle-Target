// This route is used to "reset" and delete all shots when accessing your domain or localhost: /delete-shot
// Make sure to place this snippet in /www/routes/web.php, but it can also be placed in the controller if needed

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\BulletController;

// Define the route for deleting all shots
Route::get('/delete-shot', function () {
    // Delete all shots from the database
    \App\Models\Bullet::truncate();

    // Redirect to the target page after deletion
    return redirect('/target')->with('success', 'All shots have been deleted successfully!');
});