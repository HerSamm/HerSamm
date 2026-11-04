<h1 align="center">HerSamm</h1>
<p align="center">Desarrollador .NET · Mariano Roque Alonso, Paraguay 🇵🇾</p>

<p align="center">
  <img src="assets/lenguajes.svg?v=4" alt="Tecnologías: C#, .NET, JavaScript, HTML5, CSS3, MySQL, SQL Server, Swagger y Postman" width="760"/>
</p>

## Sobre mí

- Desarrollador .NET, construyo APIs con ASP.NET Core (Minimal APIs)

## Stack

| | |
| --- | --- |
| **Lenguajes** | C#, JavaScript, HTML5, CSS |
| **Backend** | .NET, ASP.NET Core Minimal APIs |
| **Frontend** | HTML, CSS |
| **Datos** | Entity Framework Core, SQL Server, MySQL |
| **Testing** | Swagger, Postman |

## API de HerSamm

<details>
<summary><code>GET /api/perfil</code></summary>

```http
GET /api/perfil HTTP/1.1
Accept: application/json
```

```json
{
  "usuario": "HerSamm",
  "rol": "Desarrollador .NET",
  "ubicacion": "Mariano Roque Alonso, Paraguay",
  "enfoque": "APIs con ASP.NET Core (Minimal APIs)"
}
```

</details>

<details>
<summary><code>GET /api/stack</code></summary>

```http
GET /api/stack HTTP/1.1
Accept: application/json
```

```json
{
  "lenguajes": ["C#", "JavaScript", "HTML5", "CSS"],
  "backend": [".NET", "ASP.NET Core Minimal APIs"],
  "frontend": ["HTML", "CSS"],
  "datos": ["Entity Framework Core", "SQL Server", "MySQL"],
  "testing": ["Swagger", "Postman"]
}
```

</details>

<details>
<summary><code>GET /api/contacto</code></summary>

```http
GET /api/contacto HTTP/1.1
Accept: application/json
```

```json
{
  "email": "samulopez424@gmail.com",
  "linkedin": "https://www.linkedin.com/in/hermes-l%C3%B3pez-5b46b32a9"
}
```

</details>

<details>
<summary>Así se vería en C# (Minimal API)</summary>

```csharp
var app = WebApplication.Create(args);

app.MapGet("/api/perfil", () => new
{
    usuario = "HerSamm",
    rol = "Desarrollador .NET",
    ubicacion = "Mariano Roque Alonso, Paraguay",
    enfoque = "APIs con ASP.NET Core (Minimal APIs)"
});

app.MapGet("/api/stack", () => new
{
    lenguajes = new[] { "C#", "JavaScript", "HTML5", "CSS" },
    backend   = new[] { ".NET", "ASP.NET Core Minimal APIs" },
    frontend  = new[] { "HTML", "CSS" },
    datos     = new[] { "Entity Framework Core", "SQL Server", "MySQL" },
    testing   = new[] { "Swagger", "Postman" }
});

app.MapGet("/api/contacto", () => new
{
    email = "samulopez424@gmail.com",
    linkedin = "https://www.linkedin.com/in/hermes-l%C3%B3pez-5b46b32a9"
});

app.Run();
```

</details>

## Contacto

- Email: [samulopez424@gmail.com](mailto:samulopez424@gmail.com)
- LinkedIn: [Hermes López](https://www.linkedin.com/in/hermes-l%C3%B3pez-5b46b32a9)
