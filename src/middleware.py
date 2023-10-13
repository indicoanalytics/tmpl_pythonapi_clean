def after_request(response):
    response.headers.add("X-XSS-Protection", "1; mode=block")
    response.headers.add("X-Content-Type-Options", "nosniff")
    response.headers.add("X-Frame-Options", "Deny")
    response.headers.add("Cache-Control", "no-store")
    response.headers.add("Content-Security-Policy", "frame-ancestors 'none'")
    response.headers.add("Content-Security-Policy", "default-src 'none'")
    response.headers.add("Referrer-Policy", "no-referrer")
    response.headers.add("Strict-Transport-Security", "max-age=31536000; includeSubDomains; preload")

    return response