<?php
header('Content-Type: application/json');

$path = $_SERVER['REQUEST_URI'];
$method = $_SERVER['REQUEST_METHOD'];

if ($method === 'GET') {
    if (strpos($path, '/api/php/deploy') !== false) {
        echo json_encode([
            "status" => "success",
            "message" => "PHP hosting API",
            "versions" => ["7.4", "8.0", "8.1", "8.2"],
            "frameworks" => ["Laravel", "WordPress", "CodeIgniter", "Symfony"]
        ]);
    } elseif (strpos($path, '/api/php/websites') !== false) {
        echo json_encode([
            "websites" => [
                ["id" => 1, "name" => "WordPress Blog", "url" => "wp-blog.vercel.app", "status" => "active"],
                ["id" => 2, "name" => "Laravel API", "url" => "laravel-api.vercel.app", "status" => "active"]
            ]
        ]);
    } else {
        echo json_encode(["message" => "PHP Hosting API is running"]);
    }
} elseif ($method === 'POST') {
    $data = json_decode(file_get_contents('php://input'), true);
    
    if (strpos($path, '/api/php/deploy') !== false) {
        $websiteName = $data['name'] ?? 'Untitled';
        $phpVersion = $data['php_version'] ?? '8.1';
        
        echo json_encode([
            "status" => "success",
            "message" => "PHP website deployed successfully!",
            "name" => $websiteName,
            "php_version" => $phpVersion,
            "url" => "https://" . strtolower(preg_replace('/[^A-Za-z0-9]/', '-', $websiteName)) . ".vercel.app",
            "deployment_id" => bin2hex(random_bytes(8))
        ]);
    }
}
?>
