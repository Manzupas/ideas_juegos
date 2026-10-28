using UnityEngine;

public class Bullet : MonoBehaviour
{   
    public Vector2 direction = new Vector2 (1, 0);
    public float velocity = 3;
    public float ttl = 5;

    // Start is called once before the first execution of Update after the MonoBehaviour is created
    void Start()
    {
        Destroy(gameObject, ttl);
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    public void FixedUpdate()
    {
        Vector2 pos = transform.position;
        float distancia = velocity * Time.fixedDeltaTime;
        Vector2 move = direction * distancia;
        pos += move;
        transform.position = pos;   
    }
}
