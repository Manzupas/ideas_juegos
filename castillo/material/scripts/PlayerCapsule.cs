using System;
using UnityEngine;

public class PlayerCapsule : MonoBehaviour
{
    public GameObject puertaVerde;
    public GameObject puertaAzul;
    public GameObject puertaRosa;
    public GameObject puertaRelampago;

    // Start is called once before the first execution of Update after the MonoBehaviour is created
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    public void OnControllerColliderHit(ControllerColliderHit hit)
    {
        if (hit.gameObject.tag.Equals("Collectables"))
        {
            switch (hit.gameObject.name)
            {
                case "DiamanteVerde":
                    puertaVerde.GetComponent<Puerta>().abrir();
                    break;
                case "DiamanteAzul":
                    puertaAzul.GetComponent<Puerta>().abrir();
                    break;
                case "DiamanteRosa":
                    puertaRosa.GetComponent<Puerta>().abrir();
                    break;
                case "Relampago":
                    puertaRelampago.GetComponent<Puerta>().abrir();
                    break;
            }
            Destroy(hit.gameObject);
            //Debug.Log("Diamond green collected");
        }
    }
}
